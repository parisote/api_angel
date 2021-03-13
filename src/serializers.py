from typing import Optional
from graphene_pydantic import PydanticObjectType
from pydantic import BaseModel
from datetime import date


class CountryModel(BaseModel):
    id: str
    name: str


class ProvinceModel(BaseModel):
    id: int
    name: str
    country: Optional[CountryModel]


class GroupsRelationModel(BaseModel):
    id: int
    name: str


class EntityModel(BaseModel):
    name: str


class EntityMedicalInsurancePlanModel(BaseModel):
    description: str


class PersonModel(BaseModel):
    person_id: int
    last_name: str
    first_name: str
    second_last_name: str
    second_first_name: str
    sex: str
    marital_status: str
    birth: date
    country_birth: Optional[CountryModel]


class PersonCredentialModel(BaseModel):
    id: int
    credential: str
    person: Optional[PersonModel]


class PersonXGroupModel(BaseModel):
    person_id: int
    person: Optional[PersonModel]
    state: str


class PersonGroupMedicalInsurance(BaseModel):
    person_x_group: Optional[PersonXGroupModel]
    medins: Optional[EntityModel]
    medins_plan: Optional[EntityMedicalInsurancePlanModel]
    member_id: str
    state: str


class VaccineCalendarModel(BaseModel):
    code: str
    vaccine_name: str
    application_age: int
    measure_unit: str


class VaccineAplicationModel(BaseModel):
    person: Optional[PersonModel]
    vaccine: Optional[VaccineCalendarModel]


# GRAPHENE
class CountryGrapheneModel(PydanticObjectType):
    class Meta:
        model = CountryModel


class ProvinceGrapheneModel(PydanticObjectType):
    class Meta:
        model = ProvinceModel


class PersonGrapheneModel(PydanticObjectType):
    class Meta:
        model = PersonModel


class PersonCredentialGrapheneModel(PydanticObjectType):
    class Meta:
        model = PersonCredentialModel


class EntityGrapheneModel(PydanticObjectType):
    class Meta:
        model = EntityModel


class EntityMedicalInsurancePlanGrapheneModel(PydanticObjectType):
    class Meta:
        model = EntityMedicalInsurancePlanModel


class PersonXGroupGrapheneModel(PydanticObjectType):
    class Meta:
        model = PersonXGroupModel


class PersonGroupMedicalInsuranceGrapheneModel(PydanticObjectType):
    class Meta:
        model = PersonGroupMedicalInsurance


class VaccineCalendarGrapheneModel(PydanticObjectType):
    class Meta:
        model = VaccineCalendarModel


class VaccineApplicationGrapheneModel(PydanticObjectType):
    class Meta:
        model = VaccineAplicationModel
