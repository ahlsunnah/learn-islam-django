# import graphene
#
# from give_core.graphql.core.mutations import ModelMutation
# from django.shortcuts import get_object_or_404
# from give_core.charity.models import Project
# from . import inputs
#
#
# class ProjectCreate(ModelMutation):
#
#     @classmethod
#     def user_is_allowed(cls, user, input):
#         return user and user.is_authenticated and getattr(user, 'charitymanager')
#
#     @classmethod
#     def clean_input(cls, info, instance, input, errors):
#         instance.created_by = info.context.user.charitymanager
#         instance.charity = info.context.user.charitymanager.charity
#         return super().clean_input(info, instance, input, errors)
#
#     class Arguments:
#         input = inputs.ProjectInput(required=True)
#
#     class Meta:
#         model = Project
#         description="check is user is authenticated"
#         exclude = ('created_by',)
#
#
# class CharityMutation(graphene.ObjectType):
#     project_create = ProjectCreate.Field()
