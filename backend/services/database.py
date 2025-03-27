import aiosqlite


class Database:
    @staticmethod
    async def create_tables(session: aiosqlite.Connection):
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
            COMMIT TRANSACTION;
            """
        )
