from typing import NamedTuple


class Package(NamedTuple):
    id: int | None = None
    name: str | None = None
    description: str | None = None
    version: str | None = None
    author_name: str | None = None
    data: bytes | None = None
    created_at: int | None = None
    updated_at: int | None = None
