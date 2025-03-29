import aiosqlite
from functools import wraps
from typing import Callable, Awaitable


class Database:
    @staticmethod
    async def create_tables(*, session: aiosqlite.Connection):
        await session.executescript(
            """
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
        await session.commit()

    @staticmethod
    async def drop_tables(*, session: aiosqlite.Connection):
        await session.executescript(
            """
            DROP TABLE IF EXISTS packages;
            DROP INDEX IN EXISTS package_idx;
            """
        )
        await session.commit()


__all__ = ("Database",)
