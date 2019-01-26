from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from . import types


class TopicQueries(object):
    topic = relay.Node.Field(types.TopicNode)
    all_topics = DjangoFilterConnectionField(types.TopicNode)

    topic_translation = relay.Node.Field(types.TopicTranslationNode)
    all_topics_translations = DjangoFilterConnectionField(types.TopicTranslationNode)
