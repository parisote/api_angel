import graphene

from src.serializers import (
    CountryGrapheneModel,
    ProvinceGrapheneModel,
    PersonGrapheneModel,
    PersonCredentialGrapheneModel,
    PersonGroupMedicalInsuranceGrapheneModel
)

from src.models.models import Country, Province, Person, PersonCredential, PersonGroupMedicalInsurance, session


class Query(graphene.ObjectType):
    get_all_country = graphene.List(CountryGrapheneModel)
    get_country_by = graphene.Field(CountryGrapheneModel, name=graphene.NonNull(graphene.String))

    get_all_province = graphene.List(ProvinceGrapheneModel)
    get_province_by = graphene.List(ProvinceGrapheneModel, name=graphene.NonNull(graphene.String))

    get_person = graphene.List(PersonGrapheneModel, last_name=graphene.NonNull(graphene.String))
    get_person_by_credential = graphene.List(PersonCredentialGrapheneModel, credential=graphene.NonNull(graphene.String))

    get_person_medical_insurance_by_member_id = graphene.List(PersonGroupMedicalInsuranceGrapheneModel, member=graphene.NonNull(graphene.String))

    @staticmethod
    def resolve_get_all_country(parent, info):
        return session.query(Country).all()

    @staticmethod
    def resolve_get_country_by(parent, info, name):
        return session.query(Country).filter_by(id=name).first()

    @staticmethod
    def resolve_get_all_province(parent, info):
        return session.query(Province).all()

    @staticmethod
    def resolve_get_province_by(parent, info, name):
        return session.query(Province).filter_by(country_id=name)

    @staticmethod
    def resolve_get_person(parent, info, last_name=None):
        return session.query(Person).filter_by(last_name=last_name)

    @staticmethod
    def resolve_get_person_by_credential(parent, info, credential=None):
        return session.query(PersonCredential).filter_by(credential=credential)

    @staticmethod
    def resolve_get_person_medical_insurance_by_member_id(parent, info, member=None):
        return session.query(PersonGroupMedicalInsurance).filter_by(member_id=member)
