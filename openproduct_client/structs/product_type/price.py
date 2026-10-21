from collections.abc import Mapping, Sequence
from typing import Literal

from msgspec import UNSET, UnsetType

from ..base import BaseSchemaStruct

type DMNClassType = Literal[
    "String",
    "Integer",
    "Double",
    "Boolean",
    "Date",
    "Long",
]

#
# Input
#


class PriceParams(BaseSchemaStruct):
    # these are some of the available query parameters, append when/if needed
    actief_vanaf: str | UnsetType = UNSET
    actief_vanaf__gte: str | UnsetType = UNSET  # a date string (2019-09-24)
    actief_vanaf__lte: str | UnsetType = UNSET  # a date string (2019-09-24)
    producttype__uuid: str | UnsetType = UNSET


#
# Output
#


class PriceOption(BaseSchemaStruct):
    uuid: str | UnsetType = UNSET
    bedrag: str  # a decimal, with '.' as decimal separator
    beschrijving: str


class DMNMapping(BaseSchemaStruct):
    name: str
    path: str
    classType: DMNClassType


class PriceRule(BaseSchemaStruct):
    uuid: str | UnsetType = UNSET
    url: str  # uri
    beschrijving: str
    mapping: Mapping[str, Sequence[DMNMapping]] | None = (
        None  # mapping between the fields in Open Product & DMN variable
    )


class Price(BaseSchemaStruct):
    uuid: str
    producttype_uuid: str
    prijsopties: Sequence[PriceOption] | UnsetType = UNSET
    prijsregels: Sequence[PriceRule] | UnsetType = UNSET
    actief_vanaf: str  # a date string (2019-09-24)
