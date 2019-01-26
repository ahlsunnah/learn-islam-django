import graphene
import graphql_jwt

from django.http import HttpResponse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework.generics import get_object_or_404

from learn_islam.users.models import User

from .types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email, first_name, last_name):
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

#
# class VerifyEmail(graphene.Mutation):
#     user = graphene.Field(UserType)
#
#     class Arguments:
#         uidb64 = graphene.String(required=True)
#         token = graphene.String(required=True)
#
#     def mutate(self, info, uidb64, token):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#             user.save()
#
#         return VerifyEmail(user=user)

#
# class UpdateUserPassword(graphene.Mutation):
#     user = graphene.Field(UserType)
#
#     class Arguments:
#         id = graphene.String(required=True)
#         old_password = graphene.String(required=True)
#         new_password = graphene.String(required=True)
#         new_password_confirmation = graphene.String(required=True)
#
#     def mutate(self, info, id, old_password, new_password, new_password_confirmation,):
#         # TODO refactor this one port the logic to the model and raise an
#         user = User.objects.get(id=id,)
#         if not user.check_password(old_password):
#             raise Exception('Your current password is incorrect')
#
#         if new_password != new_password_confirmation:
#             raise Exception('New password and confirmation password did not match')
#
#         if new_password and len(new_password) > 6:
#             user.set_password(new_password_confirmation)
#             user.save()
#             return UpdateUserPassword(user=user)
#
#         raise Exception('Passwords should have at least 6 characters')
#
#
# class ResendEmailVerification(graphene.Mutation):
#
#     message = graphene.String()
#
#     class Arguments:
#         email = graphene.String(required=True)
#
#     def mutate(self, info, email):
#         user = get_object_or_404(User, email=email)
#         return ResendEmailVerification(message="The email verification has been sent")
#
#
#
# class UpdateUser(graphene.Mutation):
#     user = graphene.Field(UserType)
#
#     class Arguments:
#         id = graphene.String(required=True)
#         first_name = graphene.String(required=True)
#         last_name = graphene.String(required=True)
#
#     def mutate(self, info, id=None, **kwargs):
#         current_user = info.context.user
#         if not current_user.is_authenticated:
#            return HttpResponse('Unauthorized', status=401)
#
#         User.objects.filter(id=current_user.id).update(**kwargs)
#         current_user.refresh_from_db()
#         return UpdateUser(user=current_user)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    # update_user_password = UpdateUserPassword.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    # update_user = UpdateUser.Field()


