import aiosqlite
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from crud import CRUD  # type: ignore
from core import cfg  # type: ignore
from .schemas import Schemas


class PublicPackagesRouter(APIRouter):
    def __init__(self):
        super().__init__(prefix=cfg["routers_prefixes"]["public_packages"])

        @self.get("/package")
        async def get_package(schema: Schemas.GetPackage) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                if package := await CRUD.Package.get(
                    package_id=schema.package_id,
                    session=session,
                ):
                    # add "package_" prefix to keys
                    return JSONResponse(
                        {"package_" + key: value for [key, value] in package._asdict()}
                    )
                else:
                    return JSONResponse({}, status.HTTP_404_NOT_FOUND)

        @self.get("/package_info")
        async def get_package_info(schema: Schemas.GetPackageInfo) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                if package := await CRUD.Package.get_info(
                    package_id=schema.package_id,
                    session=session,
                ):
                    # add "package_" prefix to keys
                    return JSONResponse(
                        {"package_" + key: value for [key, value] in package._asdict()}
                    )
                else:
                    return JSONResponse({}, status.HTTP_404_NOT_FOUND)

        @self.get("/packages_infos")
        async def get_packages_infos(schema: Schemas.GetPackagesInfos) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                if packages := await CRUD.Package.get_packages_infos(
                    package_name=schema.package_name,
                    session=session,
                ):
                    return JSONResponse({"packages": packages})
                else:
                    return JSONResponse({}, status.HTTP_404_NOT_FOUND)


router = PublicPackagesRouter()
