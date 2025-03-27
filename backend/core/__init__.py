from typing import TypedDict
from json import load


class RoutersPrefixes(TypedDict):
    api: str


class Configuration(TypedDict):
    database_path: str
    host: str
    port: int
    routers_prefixes: RoutersPrefixes


cfg: Configuration = load(open("./backend/core/configuration.json"))

__all__ = (
    "cfg",
    "Configuration",
)
