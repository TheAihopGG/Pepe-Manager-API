from aiosqlite import connect
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from asyncio import run
from services.database import create_tables
from data.settings import *
from logging import *

__doc__ = """
GET /api/help/ - returns this text

GET /api/package/?name=<name>&version=<version>&id=< - returns package, where name=<name> and version=<version>
"""

basicConfig(
    handlers=(FileHandler(LOGS_PATH), StreamHandler()),
    format='%(levelname)s]: %(message)s',
    level=INFO
)

app = FastAPI()

@app.get('/api/help/')
async def help() -> PlainTextResponse:
    return PlainTextResponse(__doc__)

@app.get('/api/package/')
async def get_package(
    name: str | None = None,
    version: str | None = None,
    id: int | None = None
) -> JSONResponse:
    async with connect(DB_PATH) as db:
        if name and version:
            result: list[int, str] = await (await db.execute(f'''
                SELECT * FROM packages
                WHERE name=? AND version=?
            ''', (name, version))).fetchone()
        elif id:
            result: list[int, str] = await (await db.execute(f'''
                SELECT * FROM packages
                WHERE id=?
            ''', (id,))).fetchone()
        else:
            return JSONResponse({'detail':'Not provided name, version or id'}, status_code=404)

        if result:
            return JSONResponse({
                'package':dict(zip(['id', 'name', 'description', 'author', 'version', 'url'], result))
            })
        else:
            return JSONResponse({'detail':'Package not found'}, status_code=404)

if __name__ == '__main__':
    run(create_tables())
