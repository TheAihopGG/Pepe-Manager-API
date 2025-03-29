import backend.core.models as models
from typing import TypedDict
from json import load


class RoutersPrefixes(TypedDict):
    private_packages: str
    public_packages: str


class Configuration(TypedDict):
    database_path: str
    logs_path: str
    host: str
    port: int
    routers_prefixes: RoutersPrefixes
    allowed_domains: list[str]


cfg: Configuration = load(open("./backend/core/configuration.json"))

__all__ = (
    "cfg",
    "Configuration",
    "models",
)
