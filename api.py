from aiosqlite import connect
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, Response, PlainTextResponse
from fastapi.requests import Request
from asyncio import run
from services.database import create_tables
from data.settings import *
from logging import *

"""
API:
/ - return this text
/api/packages/?field=<field> - returns packages` field (METHOD: POST)
/api/package/?id=<id> or /api/package/?name=<name> - returns package info (METHOD: POST)
"""

app = FastAPI()

@app.get('/')
async def index() -> PlainTextResponse:
    return PlainTextResponse("""
        API:
        / - return this text
        /api/packages/?field=<field> - returns packages` field (METHOD: POST)
        /api/package/?id=<id> or /api/package/?name=<name> - returns package info (METHOD: POST)
    """)

@app.post('/api/packages/')
async def get_packages(field: str) -> JSONResponse:
    if field in ['id', 'name', 'author']:
        async with connect(DB_PATH) as db:
            result = await (await db.execute(f'''
                SELECT {field} FROM packages
            ''')).fetchall()
            return JSONResponse({
                'packages':[dict([(field, value)]) for value in result]
            })
    else:
        return JSONResponse({'detail':'Field must be name or author'}, status_code=404)


@app.post('/api/package/')
async def get_package(field: str, value: str) -> JSONResponse:
    async with connect(DB_PATH) as db:
        result: list[int, str, str] = await (await db.execute(f'''
            SELECT id, author, version FROM packages
            WHERE {field}=?
        ''', (value,))).fetchone()
        if result:
            return JSONResponse({
                'package':dict(zip(['id', 'author', 'version'], result))
            })
        else:
            return JSONResponse({'detail':'Package not found'}, status_code=404)
