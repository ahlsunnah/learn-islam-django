from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from . import types


class ChapterQueries(object):
    chapter = relay.Node.Field(types.ChapterNode)
    all_chapters = DjangoFilterConnectionField(types.ChapterNode)

    chapter_translations = relay.Node.Field(types.ChapterTranslationNode)
    all_chapters_translations = DjangoFilterConnectionField(types.ChapterTranslationNode)
