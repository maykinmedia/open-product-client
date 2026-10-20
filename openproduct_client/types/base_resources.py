from abc import ABCMeta
from collections.abc import Sequence
from typing import dataclass_transform

from msgspec import UNSET, Struct, StructMeta, UnsetType


@dataclass_transform(kw_only_default=True)
class ResourceMeta(StructMeta, ABCMeta):
    """
    Configure the behaviour of the resource classes.

    The metaclass avoids having to repeat a bunch of keyword arguments when defining
    msgspec structs. In particular, we establish:

    * Forbid positional arguments - many resources have a lot of properties with the -
      enforcing keyword arguments helps readability and makes things more explicit.
    """

    def __new__(mcls, name, bases, namespace, **struct_config):
        struct_config["kw_only"] = True
        cls = super().__new__(mcls, name, bases, namespace, **struct_config)
        return cls


class BaseTypeWithResourceMeta(Struct, metaclass=ResourceMeta):
    pass


class PaginationParams(BaseTypeWithResourceMeta):
    page: int | UnsetType = UNSET
    page_size: int | UnsetType = UNSET


class PaginatedResponseBody[T: Struct](BaseTypeWithResourceMeta):
    count: int
    next: str | None
    previous: str | None
    results: Sequence[T]
