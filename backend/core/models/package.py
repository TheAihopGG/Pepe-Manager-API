from typing import NamedTuple


class Package(NamedTuple):
    id: int
    name: str
    description: str
    version: str
    author_name: str
    created_at: int
    updated_at: int
