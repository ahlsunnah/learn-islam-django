import graphene

from learn_islam.graphql.courses import queries
from learn_islam.graphql.users.mutations import UserMutation


class Query(
    queries.Query,
    graphene.ObjectType,
    graphene.InputObjectType
):
    pass


class Mutation(
    UserMutation,
    graphene.ObjectType,
    graphene.InputObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
