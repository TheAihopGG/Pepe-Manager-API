from aiosqlite import connect
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from asyncio import run
from services.database import create_tables
from data.settings import *
from logging import *

__doc__ = """
GET /api/help/ - returns this text

GET /api/package_by_field/?field=<field>&value=<value> - returns package, where <field>=<value>. Supported fields: id, name, version, *

GET /api/package/?name=<name>&version=<version> - returns package, where name=<name> and version=<version>
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

@app.get('/api/package_by_field/')
async def get_package_by_field(field: str, value: str) -> JSONResponse:
    if field in ['id', 'name', 'author']:
        async with connect(DB_PATH) as db:
            result: list[int, str] = await (await db.execute(f'''
                SELECT * FROM packages
                WHERE {field}=?
            ''', (value,))).fetchone()
            if result:
                return JSONResponse({
                    'package':dict(zip(['id', 'name', 'author', 'version', 'url'], result))
                })
            else:
                return JSONResponse({'detail':'Package not found'}, status_code=404)
    else:
        return JSONResponse({'detail':'Field must be one of: name, id, author'}, status_code=404)

@app.get('/api/package/')
async def get_package(name: str, version: str) -> JSONResponse:
    async with connect(DB_PATH) as db:
        result: list[int, str] = await (await db.execute(f'''
            SELECT * FROM packages
            WHERE name=? AND version=?
        ''', (name, version))).fetchone()
        if result:
            return JSONResponse({
                'package':dict(zip(['id', 'name', 'author', 'version', 'url'], result))
            })
        else:
            return JSONResponse({'detail':'Package not found'}, status_code=404)

if __name__ == '__main__':
    run(create_tables())
