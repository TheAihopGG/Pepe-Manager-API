import aiosqlite
from time import time
from core import models
from services import Database


class CRUD:
    class Package:
        @staticmethod
        async def create(
            package_name: str,
            package_description: str,
            package_version: str,
            package_author_name: str,
            package_data: bytes,
            *,
            session: aiosqlite.Connection,
        ) -> bool:
            package = models.Package(
                id=0,
                name=package_name,
                description=package_description,
                version=package_version,
                author_name=package_author_name,
                data=package_data,
            )

            async with session.execute(
                "INSERT INTO packages (name, description, version, author_name, data, created_at, updated_at)"
                "VALUES (:name, :description, :version, :author_name, :data, :created_at, :updated_at)",
                package._asdict(),
            ) as cursor:
                await session.commit()
                return bool(cursor.rowcount)

        @staticmethod
        async def get(
            package_id: int,
            *,
            session: aiosqlite.Connection,
        ) -> models.Package | None:
            async with session.execute(
                "SELECT * FROM packages WHERE id=?",
                (package_id,),
            ) as cursor:
                result = await cursor.fetchone()
                if result:
                    package = models.Package._make(result)
                    await session.commit()
                    return package
                else:
                    return None

        @staticmethod
        async def get_info(
            package_id: int,
            *,
            session: aiosqlite.Connection,
        ) -> models.PackageInfo | None:
            async with session.execute(
                "SELECT id, name, description, version, author_name, created_at, updated_at FROM packages WHERE id=?",
                (package_id,),
            ) as cursor:
                result = await cursor.fetchone()
                if result:
                    package_info = models.PackageInfo._make(result)
                    await session.commit()
                    return package_info
                else:
                    return None

        @staticmethod
        async def update(
            package_id: int,
            package_name: str | None = None,
            package_description: str | None = None,
            package_version: str | None = None,
            package_author_name: str | None = None,
            package_data: bytes | None = None,
            *,
            session: aiosqlite.Connection,
        ) -> models.Package | None:
            package = await CRUD.Package.get(package_id, session=session)
            if package:
                updated_package = models.Package(
                    package_id,
                    name=package_name or package.name,
                    description=package_description or package.description,
                    version=package_version or package.version,
                    author_name=package_author_name or package.author_name,
                    data=package_data or package.data,
                )
                await session.execute(
                    "UPDATE packages SET name=:name, description=:description, version=:version, author_name=:author_name, data=:data, updated_at=:updated_at",
                    updated_package._asdict(),
                )
                await session.commit()
                return updated_package
            else:
                return None

        @staticmethod
        @Database.rollback_on_error
        async def delete(
            package_id: int,
            *,
            session: aiosqlite.Connection,
        ) -> models.Package | None:
            package = await CRUD.Package.get(package_id, session=session)
            if package:
                await session.execute(
                    "DELETE FROM packages WHERE id=?",
                    (package_id,),
                )

            return package


__all__ = ("CRUD",)
