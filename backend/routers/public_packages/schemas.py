from pydantic import BaseModel


class Schemas:
    class GetPackage(BaseModel):
        package_id: int

    class GetPackageInfo(BaseModel):
        package_id: int

    class GetPackagesInfos(BaseModel):
        package_name: str
