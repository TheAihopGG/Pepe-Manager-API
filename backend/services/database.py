import aiosqlite
from functools import wraps
from typing import Callable, Awaitable


class Database:
    def memory_connection(function):
        @wrapper(function)
        async def wrapper(self):
            session = await aiosqlite.connect(":memory:")
            await Database.create_tables(session)
            return await function(self, session=session)

        return wrapper

    @staticmethod
    def rollback_on_error[**P, R](
        function: Callable[P, Awaitable[R]],
    ) -> Callable[P, Awaitable[R]]:
        @wraps(function)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            session = kwargs.get("session")
            if not session or not isinstance(session, aiosqlite.Connection):
                raise ValueError(
                    "Session must be an aiosqlite.Connection and provided as keyword argument"
                )
            try:
                result = await function(*args, **kwargs)
            except Exception as err:
                await session.execute("ROLLBACK TRANSACTION")
                raise err
            else:
                await session.execute("COMMIT TRANSACTION")
                return result

        return wrapper

    @staticmethod
    @rollback_on_error
    async def create_tables(*, session: aiosqlite.Connection):
        return await session.executescript(
            """
            BEGIN TRANSACTION;
            CREATE TABLE IF NOT EXISTS packages (
                id INTEGER PRIMARY KEY,
                name VARCHAR(32),
                description VARCHAR(256),
                version VARCHAR(32),
                author_name VARCHAR(32),
                data BLOB,
                created_at INTEGER,
                updated_at INTEGER
            );
            CREATE INDEX IF NOT EXISTS package_idx ON packages(id);
            """
        )

    @staticmethod
    @rollback_on_error
    async def drop_tables(*, session: aiosqlite.Connection):
        await session.executescript(
            """
            BEGIN TRANSACTION;
            DROP TABLE IF EXISTS packages;
            DROP INDEX IN EXISTS package_idx;
            """
        )


__all__ = ("Database",)
