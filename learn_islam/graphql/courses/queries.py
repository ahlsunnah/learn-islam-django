from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from . import types


class Query(object):
    course = relay.Node.Field(types.CourseType)
    all_courses = DjangoFilterConnectionField(types.CourseType)
