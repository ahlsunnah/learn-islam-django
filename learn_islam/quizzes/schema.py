from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from . import types


class QuizQueries(object):
    quiz = relay.Node.Field(types.QuizNode)
    all_quizzes = DjangoFilterConnectionField(types.QuizNode)

    quiz_translations = relay.Node.Field(types.QuizTranslationNode)
    all_quizzes_translations = DjangoFilterConnectionField(types.QuizTranslationNode)
