import graphene

class CourseInput(graphene.InputObjectType):
    order = graphene.String()
    level = graphene.String()
    slug = graphene.String()
