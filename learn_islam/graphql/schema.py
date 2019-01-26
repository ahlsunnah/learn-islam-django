import graphene

from learn_islam.chapters.schema import ChapterQueries
from learn_islam.courses.schema import CourseQueries
from learn_islam.quizzes.schema import QuizQueries
from learn_islam.topics.schema import TopicQueries
from learn_islam.tracks.schema import TrackQueries
from learn_islam.users.mutations import UserMutation


class Query(
    ChapterQueries,
    CourseQueries,
    QuizQueries,
    TopicQueries,
    TrackQueries,
    graphene.ObjectType,
    graphene.InputObjectType
):
    pass


class Mutation(
    UserMutation,
    graphene.ObjectType,
    graphene.InputObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
