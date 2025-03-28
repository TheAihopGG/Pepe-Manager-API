from typing import NamedTuple


class PackageData(NamedTuple):
    id: int
    package_id: int
    data: bytes
