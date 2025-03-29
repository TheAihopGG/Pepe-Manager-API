import aiosqlite
from functools import wraps
from typing import Callable, Awaitable


class Database:
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
                created_at INTEGER,
                updated_at INTEGER
            );
            CREATE TABLE IF NOT EXISTS packages_dates (
                id INTEGER PRIMARY KEY,
                package_id INTEGER UNIQUE,
                data BLOB,
                FOREIGN KEY (package_id) REFERENCES packages(id)
            );
            """
        )

    @staticmethod
    @rollback_on_error
    async def drop_tables(*, session: aiosqlite.Connection):
        await session.executescript(
            """
            BEGIN TRANSACTION;
            DROP TABLE IF EXISTS packages;
            """
        )


__all__ = ("Database",)
