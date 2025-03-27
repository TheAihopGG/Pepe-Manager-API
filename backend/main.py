import aiosqlite
from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.core import cfg
from backend.services import Database


class App(FastAPI):
    @staticmethod
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with aiosqlite.connect(cfg["database_path"]) as session:
            await Database.create_tables(session)
        yield

    def __init__(self):
        super().__init__(lifespan=App.lifespan)
        self.include_routers()

    def include_routers(self):
        pass


app = App()
