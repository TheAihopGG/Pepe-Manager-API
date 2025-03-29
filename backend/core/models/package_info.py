from typing import NamedTuple
from time import time


class PackageInfo(NamedTuple):
    id: int
    name: str
    description: str
    version: str
    author_name: str
    created_at: int = int(time())
    updated_at: int = int(time())
