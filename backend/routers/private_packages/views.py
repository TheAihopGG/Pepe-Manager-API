from typing import Awaitable, Callable
from urllib.parse import urlparse
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from backend.core import cfg


def check_auth(request: Request):
    if not request.headers.get("X-Token"):
        raise HTTPException(status_code=403)


class PrivatePackagesRouter(APIRouter):
    def __init__(self):
        super().__init__(prefix=cfg["routers_prefixes"]["private_packages"])

        @self.get("/", dependencies=[Depends(check_auth)])
        async def test() -> JSONResponse:
            return JSONResponse({"success": True})


router = PrivatePackagesRouter()
