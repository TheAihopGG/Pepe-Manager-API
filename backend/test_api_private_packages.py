import unittest
import requests
import aiosqlite
from services import Database
from typing import Final
from crud import CRUD

URL: Final = "http://localhost/private/api/packages"


class TestApiPrivatePackages(unittest.IsolatedAsyncioTestCase):
    async def test_create_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        self.assertTrue(
            requests.post(
                URL + "/create",
                json={
                    "package_name": "TestPackage",
                    "package_description": "A package for testing",
                    "package_author_name": "TheAihopGG",
                    "package_version": "1.0.0",
                    "package_data": b"data",
                },
            ).ok
        )
        package = await CRUD.Package.get(
            1,
            session=session,
        )
        self.assertTrue(package)
        self.assertEqual(package.name, "TestPackage")
        self.assertEqual(package.description, "A package for testing")
        self.assertEqual(package.author_name, "TheAihopGG")
        self.assertEqual(package.version, "1.0.0")
        self.assertEqual(package.data, b"data")

    async def test_delete_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)

        self.assertTrue(
            await CRUD.Package.create(
                package_name="TestPackage",
                package_description="A package for testing",
                package_author_name="TheAihopGG",
                package_version="1.0.0",
                package_data=b"data",
                session=session,
            )
        )
        self.assertTrue(requests.delete(URL + "/delete", json={"package_id": 1}).ok)
        self.assertIsNone(await CRUD.Package.get(1, session=session))

    async def test_update_package(self):
        session = await aiosqlite.connect(":memory:")
        await Database.create_tables(session=session)
        self.assertTrue(
            await CRUD.Package.create(
                package_name="TestPackage",
                package_description="A package for testing",
                package_author_name="TheAihopGG",
                package_version="1.0.0",
                package_data=b"data",
                session=session,
            )
        )
        self.assertTrue(
            requests.put(
                URL + "/update", json={"package_id": 1, "package_version": "1.1.0"}
            ).ok
        )
        package = await CRUD.Package.get(1, session=session)
        self.assertEqual(package.version, "1.1.0")
        # we must specify an id and at least more one parameter in request body
        self.assertFalse(requests.put(URL + "/update", json={"package_id": 1}).ok)
