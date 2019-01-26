
# import pytest
# from graphql_relay import to_global_id
# from graphene_django.registry import get_global_registry

# from give_core.graphql.schema.schema import api_schema
# from graphene.test import Client
# from give_core.charity import models


# registry = get_global_registry()
#
#
# @pytest.fixture()
# def client():
#     return Client(api_schema)
#
#
# @pytest.fixture
# def rq_authenticated(rf):
#     def fun(user):
#         request = rf.get('/')
#         request.user = user
#         return request
#     return fun
#
#
# @pytest.mark.django_db
# def test_project_mutation(client, user, rq_authenticated):
#     country = models.Country.objects.create(name='kuwait')
#     category = models.Category.objects.create(title='Ramadan')
#     charity = models.Charity.objects.create(name='Give', country_id=country.id)
#     models.CharityManager.objects.create(user=user, charity=charity)
#     rq_authenticated = rq_authenticated(user)
#     mutation = """
#         mutation($ProjectInput: ProjectInput!){
#           projectCreate(input: $ProjectInput){
#             project {
#               id
#             }
#             errors {
#               field
#               message
#             }
#           }
#         }
#     """
#     result = client.execute(
#         mutation,
#         context_value=rq_authenticated,
#         variable_values={
#           "ProjectInput": {
#             "title": "Iftar Saim",
#             "description": "Tsa",
#             "targetAmount": 20000,
#             "category": to_global_id(registry.get_type_for_model(category._meta.model)._meta.name, category.id)
#           }
#         }
#     )
#
#     assert result.get('data').get('projectCreate').get('project').get('id')
