from importlib.metadata import version, PackageNotFoundError

from .base import SchemaError  # noqa: F401
from .components import (  # noqa: F401
    ArrayTypeSchema,
    AttrSchema,
    AttrsSchema,
    ChunksSchema,
    DimsSchema,
    DTypeSchema,
    NameSchema,
    ShapeSchema,
)
from .dataarray import CoordsSchema, DataArraySchema  # noqa: F401
from .dataset import DatasetSchema  # noqa: F401

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # noqa: F401; pragma: no cover
    # package is not installed
    pass
