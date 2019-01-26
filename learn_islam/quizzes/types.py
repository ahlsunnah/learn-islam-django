from graphene import relay
from graphene_django.types import DjangoObjectType

from learn_islam.quizzes import models


class QuizNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.Quiz
        filter_fields = ['difficulty', ]


class QuizTranslationNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.QuizTranslation
        filter_fields = ['locale', ]
