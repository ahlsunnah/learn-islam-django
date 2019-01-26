from graphene import relay
from graphene_django.types import DjangoObjectType

from learn_islam.chapters import models


class ChapterNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.Chapter
        filter_fields = ['slug', ]


class ChapterTranslationNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.ChapterTranslation
        filter_fields = ['locale', ]
