from collections.abc import Mapping
from typing import Literal

from msgspec import UNSET, UnsetType

from ..base import BaseSchemaStruct, PaginationParams
from . import PriceOption, PriceRule
from .common import ProductTypeAllowedStates

type TargetGroupOptions = Literal[
    "burgers",
    "interne_organisatie",
    "samenwerkingspartners",
    "bedrijven_en_instellingen",
]

#
# Common
#


class NestedExternalCode(BaseSchemaStruct):
    naam: str
    code: str


class NestedParameters(BaseSchemaStruct):
    naam: str
    waarde: str


class NestedCaseType(BaseSchemaStruct):
    urn: str | None = None
    url: str | None = None  # uri


class NestedRequestType(BaseSchemaStruct):
    urn: str | None = None
    url: str | None = None  # uri


class NestedProcess(BaseSchemaStruct):
    urn: str | None = None
    url: str | None = None  # uri


#
# Input
#


class ProductTypeParams(PaginationParams):
    # these are some of the available query parameters, append when/if needed
    aanmaak_datum: str | UnsetType = (
        UNSET  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    )
    code: str | UnsetType = UNSET
    gepubliceerd: bool | UnsetType = UNSET
    keywords: list[str] | UnsetType = UNSET
    naam: str | UnsetType = UNSET
    themas__naam: str | UnsetType = UNSET
    themas__uuid: str | UnsetType = UNSET
    toegestane_statussen: list[ProductTypeAllowedStates] | UnsetType = UNSET


class ContentParams(PaginationParams):
    exclude_labels: list[str] | UnsetType = UNSET
    labels: list[str] | UnsetType = UNSET


class ProductTypeCreateData(BaseSchemaStruct):
    uniforme_product_naam: str | None = None
    doelgroep: TargetGroupOptions
    thema_uuids: list[str] | UnsetType = UNSET
    locatie_uuids: list[str] | UnsetType = UNSET
    organisatie_uuids: list[str] | UnsetType = UNSET
    # facetten_uuids: list[str] | UnsetType = UNSET
    eigenaar: str | None = None
    contact_uuids: list[str] | UnsetType = UNSET
    naam: str
    samenvatting: str
    externe_codes: list[NestedExternalCode] | UnsetType = UNSET
    parameters: list[NestedParameters] | UnsetType = UNSET
    verbruiksobject_schema_naam: str | UnsetType = UNSET
    dataobject_schema_naam: str | UnsetType = UNSET
    publicatie_start_datum: str | None = None
    publicatie_eind_datum: str | None = None
    code: str
    toegestane_statussen: list[ProductTypeAllowedStates] | UnsetType = UNSET
    keywords: list[str] | UnsetType = UNSET
    interne_opmerkingen: str | UnsetType = UNSET
    zaaktypen: list[NestedCaseType] | UnsetType = UNSET
    verzoektypen: list[NestedRequestType] | UnsetType = UNSET
    processen: list[NestedProcess] | UnsetType = UNSET


class ProductTypePartialUpdateData(BaseSchemaStruct):
    uniforme_product_naam: str | None = None
    doelgroep: TargetGroupOptions | UnsetType = UNSET
    thema_uuids: list[str] | UnsetType = UNSET
    locatie_uuids: list[str] | UnsetType = UNSET
    organisatie_uuids: list[str] | UnsetType = UNSET
    # facetten_uuids: list[str] | UnsetType = UNSET
    eigenaar: str | None = None
    contact_uuids: list[str] | UnsetType = UNSET
    naam: str | UnsetType = UNSET
    samenvatting: str | UnsetType = UNSET
    externe_codes: list[NestedExternalCode] | UnsetType = UNSET
    parameters: list[NestedParameters] | UnsetType = UNSET
    verbruiksobject_schema_naam: str | UnsetType = UNSET
    dataobject_schema_naam: str | UnsetType = UNSET
    publicatie_start_datum: str | None = None
    publicatie_eind_datum: str | None = None
    code: str | UnsetType = UNSET
    toegestane_statussen: list[ProductTypeAllowedStates] | UnsetType = UNSET
    keywords: list[str] | UnsetType = UNSET
    interne_opmerkingen: str | UnsetType = UNSET
    zaaktypen: list[NestedCaseType] | UnsetType = UNSET
    verzoektypen: list[NestedRequestType] | UnsetType = UNSET
    processen: list[NestedProcess] | UnsetType = UNSET


#
# Output
#


class NestedContentElement(BaseSchemaStruct):
    uuid: str
    taal: str
    content: str
    aanvullende_informatie: str | UnsetType = UNSET
    labels: list[str] | UnsetType = UNSET


class NestedTheme(BaseSchemaStruct):
    uuid: str
    naam: str
    beschrijving: str | UnsetType = UNSET
    gepubliceerd: bool | UnsetType = UNSET
    aanmaak_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    update_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    hoofd_thema: str | None = None


class Location(BaseSchemaStruct):
    uuid: str
    naam: str
    email: str | UnsetType = UNSET
    telefoonnummer: str | UnsetType = UNSET
    straat: str | UnsetType = UNSET
    huisnummer: str | UnsetType = UNSET
    postcode: str | UnsetType = UNSET
    stad: str | UnsetType = UNSET


class Organization(BaseSchemaStruct):
    uuid: str
    naam: str
    code: str
    email: str | UnsetType = UNSET
    telefoonnummer: str | UnsetType = UNSET
    straat: str | UnsetType = UNSET
    huisnummer: str | UnsetType = UNSET
    postcode: str | UnsetType = UNSET
    stad: str | UnsetType = UNSET


class Contact(BaseSchemaStruct):
    uuid: str
    organisatie: Organization | None = None
    naam: str
    email: str | UnsetType = UNSET
    telefoonnummer: str | UnsetType = UNSET
    rol: str | UnsetType = UNSET


class NestedPrice(BaseSchemaStruct):
    uuid: str
    prijsopties: list[PriceOption] | UnsetType = UNSET
    prijsregels: list[PriceRule] | UnsetType = UNSET
    actief_vanaf: str  # a date string (2019-09-24)


class NestedLink(BaseSchemaStruct):
    uuid: str
    naam: str
    url: str  # uri


class NestedAction(BaseSchemaStruct):
    uuid: str
    naam: str
    url: str  # uri
    mapping: Mapping | None = (
        None  # mapping between the fields in Open Product & DMN variable
    )


class NestedFile(BaseSchemaStruct):
    uuid: str
    bestand: str  # uri


class ConsumableSchema(BaseSchemaStruct):
    naam: str
    schema: Mapping


class DataObjectSchema(BaseSchemaStruct):
    naam: str
    schema: Mapping


class ProductType(BaseSchemaStruct):
    uuid: str
    uniforme_product_naam: str | None = None
    doelgroep: TargetGroupOptions
    themas: list[NestedTheme]
    locaties: list[Location]
    organisaties: list[Organization]
    eigenaar: str | None = None
    contacten: list[Contact]
    prijzen: list[NestedPrice]
    links: list[NestedLink]
    acties: list[NestedAction]
    bestanden: list[NestedFile]
    naam: str
    samenvatting: str
    taal: str
    externe_codes: list[NestedExternalCode] | UnsetType = UNSET
    parameters: list[NestedParameters] | UnsetType = UNSET
    verbruiksobject_schema: ConsumableSchema | None
    dataobject_schema: DataObjectSchema | None
    gepubliceerd: bool
    publicatie_start_datum: str | None = None  # a date string (2019-09-24)
    publicatie_eind_datum: str | None = None  # a date string (2019-09-24)
    aanmaak_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    update_datum: str  # a date-time ISO 8601 string (2019-08-24T14:15:22Z)
    code: str
    toegestane_statussen: list[ProductTypeAllowedStates] | UnsetType = UNSET
    keywords: list[str] | UnsetType = UNSET
    interne_opmerkingen: str | UnsetType = UNSET
    zaaktypen: list[NestedCaseType] | UnsetType = UNSET
    verzoektypen: list[NestedRequestType] | UnsetType = UNSET
    processen: list[NestedProcess] | UnsetType = UNSET
