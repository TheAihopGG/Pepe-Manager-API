import unittest
import requests
import aiosqlite
from core import cfg
from services import Database
from typing import Final
from crud import CRUD

URL: Final = "http://localhost:8000/private/api/packages"


class TestApiPrivatePackages(unittest.IsolatedAsyncioTestCase):
    async def test_create_package(self):
        session = await aiosqlite.connect(cfg["database_path"])
        await Database.create_tables(session=session)
        self.assertTrue(
            requests.post(
                URL + "/create",
                json={
                    "package_name": "TestPackage",
                    "package_description": "A package for testing",
                    "package_author_name": "TheAihopGG",
                    "package_version": "1.0.0",
                    "package_data": "data",
                },
            ).ok
        )

    async def test_delete_package(self):
        session = await aiosqlite.connect(cfg["database_path"])
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

    async def test_update_package(self):
        session = await aiosqlite.connect(cfg["database_path"])
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


unittest.main()
