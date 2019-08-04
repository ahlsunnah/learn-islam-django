from learn_islam.users.models import User
from graphene_django.types import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password", "email")
