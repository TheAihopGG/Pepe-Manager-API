import aiosqlite
import logging
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from core import cfg  # type: ignore
from crud import CRUD  # type: ignore
from .schemas import Schemas


class PrivatePackagesRouter(APIRouter):
    def __init__(self):
        super().__init__(prefix=cfg["routers_prefixes"]["private_packages"])
        logging.debug("test")

        @self.post("/create")
        async def create_packages(schema: Schemas.CreatePackage) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                if await CRUD.Package.create(
                    **schema.model_dump(),
                    session=session,
                ):
                    return JSONResponse({})
                else:
                    return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        @self.delete("/delete")
        async def delete_package(schema: Schemas.DeletePackage) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                if await CRUD.Package.delete(schema.package_id, session=session):
                    return JSONResponse({})
                else:
                    return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        @self.put("/update")
        async def update_package(schema: Schemas.UpdatePackage) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                print(schema.model_fields_set)
                if (
                    len(schema.model_fields_set) >= 2
                ):  # user must specify an id and something else
                    if await CRUD.Package.update(
                        **schema.model_dump(),
                        session=session,
                    ):
                        return JSONResponse({})
                    else:
                        return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return JSONResponse(
                        {
                            "detail": "you must specify an id and at least more one parameter"
                        },
                        status.HTTP_400_BAD_REQUEST,
                    )


router = PrivatePackagesRouter()
