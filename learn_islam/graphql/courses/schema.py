from graphene_django.types import DjangoObjectType

from learn_islam.courses import models


class CourseType(DjangoObjectType):
    class Meta:
        model = models.Course
