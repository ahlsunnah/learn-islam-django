import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from learn_islam.quizzes import models


class QuizNode(DjangoObjectType):
    type = graphene.String()

    class Meta:
        interfaces = (relay.Node,)
        model = models.Quiz
        filter_fields = ['difficulty', 'type' ]


class QuizTranslationNode(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = models.QuizTranslation
        filter_fields = ['locale', ]
