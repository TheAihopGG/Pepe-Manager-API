import unittest
import requests
import aiosqlite
from core import cfg
from services import Database
from typing import Final
from crud import CRUD

URL: Final = "http://localhost:8000/public/api/packages"


class TestApiPrivatePackages(unittest.IsolatedAsyncioTestCase):
    async def test_get_package(self):
        session = await aiosqlite.connect(cfg["database_path"])

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
        response = requests.get(URL + "/package", json={"package_id": 1})
        self.assertTrue(response.ok)
        package = response.json()
        self.assertTrue(package)

        self.assertEqual(package["package_name"], "TestPackage")
        self.assertEqual(package["package_description"], "A package for testing")
        self.assertEqual(package["package_author_name"], "TheAihopGG")
        self.assertEqual(package["package_version"], "1.0.0")

        await CRUD.Package.delete(
            package_id=1,
            session=session,
        )

    async def test_get_package_info(self):
        session = await aiosqlite.connect(cfg["database_path"])

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
        response = requests.get(URL + "/package_info", json={"package_id": 1})
        self.assertTrue(response.ok)
        package = response.json()
        self.assertTrue(package)

        self.assertEqual(package["package_name"], "TestPackage")
        self.assertEqual(package["package_description"], "A package for testing")
        self.assertEqual(package["package_author_name"], "TheAihopGG")
        self.assertEqual(package["package_version"], "1.0.0")
        self.assertFalse("data" in package)
        await CRUD.Package.delete(
            package_id=1,
            session=session,
        )

    async def test_get_packages_infos(self):
        session = await aiosqlite.connect(cfg["database_path"])

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
            await CRUD.Package.create(
                package_name="TestPackage",
                package_description="A package for testing",
                package_author_name="TheAihopGG",
                package_version="2.0.0",
                package_data=b"data",
                session=session,
            )
        )
        self.assertTrue(
            await CRUD.Package.create(
                package_name="TestPackage",
                package_description="A package for testing",
                package_author_name="TheAihopGG",
                package_version="3.0.0",
                package_data=b"data",
                session=session,
            )
        )
        response = requests.get(
            URL + "/packages_infos", json={"package_name": "TestPackage"}
        )
        self.assertTrue(response.ok)
        data = response.json()
        self.assertTrue(data)
        packages = data["packages"]
        for package in packages:
            self.assertEqual(package["name"], "TestPackage")

        await CRUD.Package.delete(
            package_id=1,
            session=session,
        )
        await CRUD.Package.delete(
            package_id=2,
            session=session,
        )
        await CRUD.Package.delete(
            package_id=3,
            session=session,
        )


unittest.main()
