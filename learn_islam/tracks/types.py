import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from learn_islam.tracks import models


class TrackNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.Track
        filter_fields = ['slug', ]


class TrackTranslationNode(DjangoObjectType):
    locale = graphene.String()

    class Meta:
        interfaces = (relay.Node,)
        model = models.TrackTranslation
        filter_fields = ['locale', ]
