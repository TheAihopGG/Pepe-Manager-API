from aiosqlite import connect
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, Response, PlainTextResponse
from fastapi.requests import Request
from asyncio import run
from services.database import create_tables
from data.settings import *

"""
API:
/ - return this text
/api/packages/?field=<field> - returns packages` field (METHOD: POST)
/api/package/?id=<id> or /api/package/?name=<name> - returns package info (METHOD: POST)
"""

app = FastAPI()

@app.get('/')
async def index() -> PlainTextResponse:
    return PlainTextResponse(__doc__)

@app.post('/api/packages/')
async def get_packages(field: str) -> (JSONResponse | PlainTextResponse):
    if field in ['name', 'author']:
        async with connect(DB_PATH) as db:
            result = await (await db.execute(f'''
                SELECT {field} FROM packages
            ''')).fetchone()
            return JSONResponse({
                'packages':[dict(field=values[0]) for values in result]
            })
    else:
        return PlainTextResponse('Field must be name or author', status_code=404)


@app.post('/api/package/')
async def get_package(name: str) -> (JSONResponse | PlainTextResponse):
    async with connect(DB_PATH) as db:
        result: list[int, str, str] = await (await db.execute('''
            SELECT id, author, version FROM packages
            WHERE name=?
        ''', (name,))).fetchone()
        if result:
            return JSONResponse({
                'package':dict(zip(['id', 'author', 'version'], result))
            })
        else:
            return PlainTextResponse('Package not found', status_code=404)


@app.post('/api/package/')
async def get_package(id: int) -> (JSONResponse | PlainTextResponse):
    async with connect(DB_PATH) as db:
        result: list[str, str, str] = await (await db.execute('''
            SELECT name, author, version FROM packages
            WHERE id=?
        ''', (id,))).fetchone()
        if result:
            return JSONResponse({
                'package':dict(zip(['name', 'author', 'version'], result))
            })
        else:
            return PlainTextResponse('Package not found', status_code=404)

if __name__ == '__main__':
    run(create_tables())
