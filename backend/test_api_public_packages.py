import unittest
import requests
import aiosqlite
from services import Database
from typing import Final
from crud import CRUD

URL: Final = "http://localhost/public/api/packages"


class TestApiPrivatePackages(unittest.IsolatedAsyncioTestCase):
    async def test_get_package(self):
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
        response = requests.get(URL + "/package", json={"package_id": 1})
        self.assertTrue(response.ok)
        package = response.json()
        self.assertTrue(package)

        self.assertEqual(package.name, "TestPackage")
        self.assertEqual(package.description, "A package for testing")
        self.assertEqual(package.author_name, "TheAihopGG")
        self.assertEqual(package.version, "1.0.0")
        self.assertEqual(package.data, b"data")

    async def test_get_package_info(self):
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
        response = requests.get(URL + "/package_info", json={"package_id": 1})
        self.assertTrue(response.ok)
        package = response.json()
        self.assertTrue(package)

        self.assertEqual(package.name, "TestPackage")
        self.assertEqual(package.description, "A package for testing")
        self.assertEqual(package.author_name, "TheAihopGG")
        self.assertEqual(package.version, "1.0.0")
        self.assertFalse("data" in package)

    async def test_get_packages_infos(self):
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
            match package["id"]:
                case 1:
                    self.assertEqual(package["version"], "1.0.0")
                case 2:
                    self.assertEqual(package["version"], "2.0.0")
                case 3:
                    self.assertEqual(package["version"], "3.0.0")
