from graphene import relay
from graphene_django.types import DjangoObjectType

from learn_islam.courses import models


class CourseType(DjangoObjectType):

    class Meta:
        interfaces = (relay.Node,)
        model = models.Course
        filter_fields = ['slug', ]
