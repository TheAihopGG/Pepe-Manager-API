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
                        {
                            "package_id": package.id,
                            "package_name": package.name,
                            "package_description": package.description,
                            "package_version": package.version,
                            "package_author_name": package.author_name,
                            "package_data": str(package.data),
                            "package_created_at": package.created_at,
                            "package_updated_at": package.updated_at,
                        }
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
                        {
                            "package_id": package.id,
                            "package_name": package.name,
                            "package_description": package.description,
                            "package_version": package.version,
                            "package_author_name": package.author_name,
                            "package_created_at": package.created_at,
                            "package_updated_at": package.updated_at,
                        }
                    )
                else:
                    return JSONResponse({}, status.HTTP_404_NOT_FOUND)

        @self.get("/packages_info")
        async def get_packages_info(schema: Schemas.GetPackagesInfos) -> JSONResponse:
            async with aiosqlite.connect(cfg["database_path"]) as session:
                if packages := await CRUD.Package.get_packages_info(
                    package_name=schema.package_name,
                    session=session,
                ):
                    return JSONResponse(
                        {
                            "packages": list(
                                map(
                                    lambda package_model: package_model._asdict(),
                                    packages,
                                )
                            )
                        }
                    )
                else:
                    return JSONResponse({}, status.HTTP_404_NOT_FOUND)


router = PublicPackagesRouter()
