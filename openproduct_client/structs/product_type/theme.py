from msgspec import UNSET, UnsetType

from ..base import BaseSchemaStruct, PaginationParams
from .common import ProductTypeAllowedStates

#
# Input
#


class ThemeParams(PaginationParams):
    # these are some of the available query parameters, append when/if needed
    aanmaak_datum: str | UnsetType = (
        UNSET  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    )
    gepubliceerd: bool | UnsetType = UNSET
    naam: str | UnsetType = UNSET
    producttypen__uuid: str | UnsetType = UNSET
    update_datum: str | UnsetType = (
        UNSET  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    )


class ContentThemeParams(PaginationParams):
    exclude_labels: list[str] | UnsetType = UNSET
    labels: list[str] | UnsetType = UNSET


#
# Output
#


class NestedProductType(BaseSchemaStruct):
    uuid: str
    code: str
    naam: str
    uniforme_product_naam: str
    toegestane_statussen: list[ProductTypeAllowedStates] | None = None
    gepubliceerd: bool
    aanmaak_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    update_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    taal: str
    keywords: list[str] | None = None
    publicatie_start_datum: str | None = None  # a date string (2019-09-24)
    publicatie_eind_datum: str | None = None  # a date string (2019-09-24)


class Theme(BaseSchemaStruct):
    uuid: str
    naam: str
    beschrijving: str | None = None
    gepubliceerd: bool | None = None
    aanmaak_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    update_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    hoofd_thema: str | None = None
    producttypen: list[NestedProductType]
