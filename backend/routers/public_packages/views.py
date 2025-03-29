from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from core import cfg


class PublicPackagesRouter(APIRouter):
    def __init__(self):
        super().__init__(prefix=cfg["routers_prefixes"]["public_packages"])


router = PublicPackagesRouter()
