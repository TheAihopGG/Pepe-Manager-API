import unittest
import aiosqlite
from time import time
from core import models
from services import Database
from crud import CRUD


class TestPackageCRUD(unittest.IsolatedAsyncioTestCase):
    async def test_create_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        created_package = models.Package(
            id=1,
            name="test-package-stable",
            description="Package for tests",
            version="1.1.1",
            author_name="TheAihopGG",
            data=b"data",
            created_at=int(time()),
            updated_at=int(time()),
        )

        self.assertTrue(
            await CRUD.Package.create(
                package_name=created_package.name,
                package_description=created_package.description,
                package_author_name=created_package.author_name,
                package_data=created_package.data,
                package_version=created_package.version,
                session=session,
            )
        )
        async with session.execute(
            "SELECT * FROM packages WHERE id=?", (created_package.id,)
        ) as cursor:
            result = await cursor.fetchone()
            self.assertTrue(result)
            package = models.Package._make(result)
            # compare package and created_package
            self.assertDictEqual(
                created_package._asdict(),
                package._asdict(),
            )

    async def test_get_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        created_package = models.Package(
            id=1,
            name="test-package-stable",
            description="Package for tests",
            version="1.1.1",
            author_name="TheAihopGG",
            data=b"data",
            created_at=int(time()),
            updated_at=int(time()),
        )
        await session.execute(
            "INSERT INTO packages (name, description, version, author_name, data, created_at, updated_at)"
            "VALUES (:name, :description, :version, :author_name, :data, :created_at, :updated_at)",
            created_package._asdict(),
        )
        await session.commit()
        package = await CRUD.Package.get(created_package.id, session=session)
        self.assertTrue(package)
        if package:
            self.assertDictEqual(
                created_package._asdict(),
                package._asdict(),
            )

    async def test_get_package_info(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        created_package = models.Package(
            id=1,
            name="test-package-stable",
            description="Package for tests",
            version="1.1.1",
            author_name="TheAihopGG",
            data=b"data",
            created_at=int(time()),
            updated_at=int(time()),
        )
        create_package_info = models.PackageInfo(
            id=1,
            name="test-package-stable",
            description="Package for tests",
            version="1.1.1",
            author_name="TheAihopGG",
            created_at=int(time()),
            updated_at=int(time()),
        )
        await session.execute(
            "INSERT INTO packages (name, description, version, author_name, data, created_at, updated_at)"
            "VALUES (:name, :description, :version, :author_name, :data, :created_at, :updated_at)",
            created_package._asdict(),
        )
        await session.commit()
        package_info = await CRUD.Package.get_info(created_package.id, session=session)
        self.assertTrue(package_info)
        if package_info:
            self.assertDictEqual(
                create_package_info._asdict(),
                package_info._asdict(),
            )

    async def test_get_packages_info(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        created_packages = [
            models.Package(
                id=1,
                name="test-package-stable",
                description="Package for tests",
                version="1.1.1",
                author_name="TheAihopGG",
                data=b"data",
            ),
            models.Package(
                id=2,
                name="test-package-stable",
                description="Package for tests",
                version="1.1.2",
                author_name="TheAihopGG",
                data=b"data",
            ),
            models.Package(
                id=3,
                name="test-package-stable",
                description="Package for tests",
                version="1.1.3",
                author_name="TheAihopGG",
                data=b"data",
            ),
        ]
        for created_package in created_packages:
            await session.execute(
                "INSERT INTO packages (name, description, version, author_name, data, created_at, updated_at)"
                "VALUES (:name, :description, :version, :author_name, :data, :created_at, :updated_at)",
                created_package._asdict(),
            )
        await session.commit()
        packages = await CRUD.Package.get_packages_info(
            "test-package-stable",
            session=session,
        )
        self.assertEqual(
            [created_package.version for created_package in created_packages],
            [package.version for package in packages],
        )

    async def test_update_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        created_package = models.Package(
            id=1,
            name="test-package-stable",
            description="Package for tests",
            version="1.1.1",
            author_name="TheAihopGG",
            data=b"data",
            created_at=int(time()),
            updated_at=int(time()),
        )
        await session.execute(
            "INSERT INTO packages (name, description, version, author_name, data, created_at, updated_at)"
            "VALUES (:name, :description, :version, :author_name, :data, :created_at, :updated_at)",
            created_package._asdict(),
        )
        await session.commit()
        updated_package = await CRUD.Package.update(
            package_id=1,
            package_version="2.0.0",
            session=session,
        )
        async with session.execute(
            "SELECT * FROM packages WHERE id=?", (created_package.id,)
        ) as cursor:
            result = await cursor.fetchone()
            self.assertTrue(result)
            self.assertTrue(updated_package)
            if updated_package and result:
                package = models.Package._make(result)
                self.assertDictEqual(
                    updated_package._asdict(),
                    package._asdict(),
                )

    async def test_delete_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        created_package = models.Package(
            id=1,
            name="test-package-stable",
            description="Package for tests",
            version="1.1.1",
            author_name="TheAihopGG",
            data=b"data",
            created_at=int(time()),
            updated_at=int(time()),
        )
        await session.execute(
            "INSERT INTO packages (name, description, version, author_name, data, created_at, updated_at)"
            "VALUES (:name, :description, :version, :author_name, :data, :created_at, :updated_at)",
            created_package._asdict(),
        )
        await session.commit()
        await CRUD.Package.delete(
            created_package.id,
            session=session,
        )
        async with session.execute(
            "SELECT * FROM packages WHERE id=?", (created_package.id,)
        ) as cursor:
            result = await cursor.fetchone()
            self.assertFalse(result)


unittest.main()
