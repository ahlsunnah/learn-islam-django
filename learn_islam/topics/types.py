from graphene import relay
from graphene_django.types import DjangoObjectType

from learn_islam.topics import models


class TopicNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.Topic
        filter_fields = ['slug', ]


class TopicTranslationNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.TopicTranslation
        filter_fields = ['locale', ]
