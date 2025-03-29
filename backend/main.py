from typing import Callable, Awaitable
from urllib.parse import urlparse
from fastapi.middleware.cors import CORSMiddleware
import aiosqlite
import logging
from backend.routers import (
    public_packages,
    private_packages,
)
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, Response
from fastapi import status
from backend.core import cfg
from backend.services import Database

logging.basicConfig(
    handlers=(
        logging.FileHandler(cfg["logs_path"], mode="w"),
        logging.StreamHandler(),
    ),
    format="%(asctime)s: %(levelname)s: %(message)s",
    datefmt="%m.%d.%Y %H:%M:%S",
    level=logging.INFO,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with aiosqlite.connect(cfg["database_path"]) as session:
        await Database.create_tables(session=session)
    yield


class App(FastAPI):
    def __init__(self):
        super().__init__()
        self.mount("/public", PublicApp())
        self.mount("/private", PrivateApp())


class PublicApp(FastAPI):
    def __init__(self):
        super().__init__(lifespan=lifespan)
        self.include_router(public_packages.router)


class PrivateApp(FastAPI):
    def __init__(self):
        super().__init__()
        self.include_router(private_packages.router)
        self.add_middleware(
            CORSMiddleware,
            allow_origins=cfg["allowed_domains"],
            allow_methods=["*"],
        )


app = App()
