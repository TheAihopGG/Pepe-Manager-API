from aiosqlite import connect
from os.path import exists
from data.settings import DB_PATH


async def create_tables(db_path: str = DB_PATH):
    """
    Creates these tables: packages
    Args:
    db_path - path to database. Default DB_PATH from settings.py
    """
    assert exists(db_path)
    # connection
    async with connect(db_path) as db:
        await db.executescript('''
            CREATE TABLE IF NOT EXISTS packages (
                id INTEGER PRIMARY KEY,
                name TEXT,
                author TEXT,
                version TEXT
            );
        ''')
