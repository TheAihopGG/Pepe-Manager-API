from typing import Awaitable, Callable
from urllib.parse import urlparse
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from core import cfg
from .schemas import Schemas


class PrivatePackagesRouter(APIRouter):
    def __init__(self):
        super().__init__(prefix=cfg["routers_prefixes"]["private_packages"])


router = PrivatePackagesRouter()
