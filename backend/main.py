import aiosqlite
import logging
import uvicorn
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from routers import (
    public_packages,
    private_packages,
)
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from core import cfg
from services import Database

logging.basicConfig(
    handlers=(
        logging.FileHandler(cfg["logs_path"], mode="w"),
        logging.StreamHandler(),
    ),
    format="%(asctime)s: %(levelname)s: %(message)s",
    datefmt="%m.%d.%Y %H:%M:%S",
    level=logging.INFO,
)


class App(FastAPI):
    @staticmethod
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with aiosqlite.connect(cfg["database_path"]) as session:
            await Database.create_tables(session=session)
        yield

    def __init__(self):
        super().__init__(lifespan=App.lifespan)
        self.mount("/public", PublicApp())
        self.mount("/private", PrivateApp())


class PublicApp(FastAPI):
    def __init__(self):
        super().__init__()
        self.include_router(public_packages.router)


class PrivateApp(FastAPI):
    def __init__(self):
        super().__init__()
        self.include_router(private_packages.router)
        self.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=cfg["allowed_domains"],
        )


app = App()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=cfg["host"],
        port=cfg["port"],
        reload=True,
    )
