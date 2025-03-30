from pydantic import BaseModel


class Schemas:
    class CreatePackage(BaseModel):
        package_name: str
        package_description: str
        package_version: str
        package_author_name: str
        package_data: str

    class DeletePackage(BaseModel):
        package_id: int

    class UpdatePackage(BaseModel):
        package_id: int
        package_name: str | None = None
        package_description: str | None = None
        package_version: str | None = None
        package_author_name: str | None = None
        package_data: str | None = None
