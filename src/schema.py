import graphene
from sqlalchemy_paginator import Paginator

from src.serializers import (
    CountryGrapheneModel,
    ProvinceGrapheneModel,
    PersonGrapheneModel,
    PersonCredentialGrapheneModel,
    PersonGroupMedicalInsuranceGrapheneModel,
    VaccineApplicationGrapheneModel
)

from src.models.models import Country, Province, Person, PersonCredential, PersonGroupMedicalInsurance, VaccineApplication, VaccineCalendar, session


class Query(graphene.ObjectType):
    get_all_country = graphene.List(CountryGrapheneModel)
    get_country_by = graphene.Field(CountryGrapheneModel, name=graphene.NonNull(graphene.String))

    get_all_province = graphene.List(ProvinceGrapheneModel)
    get_province_by = graphene.List(ProvinceGrapheneModel, name=graphene.NonNull(graphene.String))

    get_person = graphene.List(PersonGrapheneModel, last_name=graphene.NonNull(graphene.String))
    get_person_by_credential = graphene.List(PersonCredentialGrapheneModel, credential=graphene.NonNull(graphene.String))

    get_person_medical_insurance_by_member_id = graphene.List(PersonGroupMedicalInsuranceGrapheneModel, member=graphene.NonNull(graphene.String))
    get_person_medical_insurance_by_state = graphene.List(PersonGroupMedicalInsuranceGrapheneModel, state=graphene.NonNull(graphene.String))

    get_vaccine_aplication_by_person_id = graphene.List(VaccineApplicationGrapheneModel, person_id=graphene.NonNull(graphene.Int))
    get_vaccine_aplication_by_code = graphene.List(VaccineApplicationGrapheneModel, code=graphene.NonNull(graphene.String))

    @staticmethod
    def resolve_get_all_country(parent, info):
        q = session.query(Country)
        return q.all()

    @staticmethod
    def resolve_get_country_by(parent, info, name):
        q = session.query(Country).filter_by(id=name).first()
        return q.all()

    @staticmethod
    def resolve_get_all_province(parent, info):
        q = session.query(Province)
        return q.all()

    @staticmethod
    def resolve_get_province_by(parent, info, name):
        q = session.query(Province).filter_by(country_id=name)
        return q.all()

    @staticmethod
    def resolve_get_person(parent, info, last_name=None):
        q = session.query(Person).filter_by(last_name=last_name)
        return q.all()

    @staticmethod
    def resolve_get_person_by_credential(parent, info, credential=None):
        q = session.query(PersonCredential).filter_by(credential=credential)
        return q.all()

    @staticmethod
    def resolve_get_person_medical_insurance_by_member_id(parent, info, member=None):
        q = session.query(PersonGroupMedicalInsurance).filter_by(member_id=member)
        return q.all()

    @staticmethod
    def resolve_get_person_medical_insurance_by_state(parent, info, state=None):
        return session.query(PersonGroupMedicalInsurance).filter_by(state=state).all()

    @staticmethod
    def resolve_get_vaccine_aplication_by_person_id(parent, info, person_id=None):
        return session.query(VaccineApplication).filter_by(person_id=person_id).all()

    @staticmethod
    def resolve_get_vaccine_aplication_by_code(parent, info, code=None):
        return session.query(VaccineCalendar).filter_by(code=code).all()
