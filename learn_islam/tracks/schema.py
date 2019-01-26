from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from . import types


class TrackQueries(object):
    track = relay.Node.Field(types.TrackNode)
    all_tracks = DjangoFilterConnectionField(types.TrackNode)

    track_translation = relay.Node.Field(types.TrackTranslationNode)
    all_tracks_translations = DjangoFilterConnectionField(types.TrackTranslationNode)
