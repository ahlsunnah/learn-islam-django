# -*- coding: utf-8 -*-
import decimal
import graphene


class Decimal(graphene.Float):
    """Custom Decimal implementation.
    Returns Decimal as a float in the API,
    parses float to the Decimal on the way back.
    """

    @staticmethod
    def parse_literal(node):
        try:
            return decimal.Decimal(node.value)
        except decimal.DecimalException:
            return None

    @staticmethod
    def parse_value(value):
        try:
            # Converting the float to str before parsing it to Decimal is
            # necessary to keep the decimal places as typed
            value = str(value)
            return decimal.Decimal(value)
        except decimal.DecimalException:
            return None


class Upload(graphene.types.Scalar):
    @staticmethod
    def serialize(value):
        return value

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value


class Error(graphene.ObjectType):
    field = graphene.String(
        description="""Name of a field that caused the error. A value of
        `null` indicates that the error isn't associated with a particular
        field.""", required=False)
    message = graphene.String(description='The error message.')

    class Meta:
        description = 'Represents an error in the input of a mutation.'


class Image(graphene.ObjectType):
    url = graphene.String(
        required=True,
        description='The URL of the image.'
    )

    class Meta:
        description = 'Represents an image.'

    def resolve_url(self, info):
        return self.url


class File(graphene.ObjectType):
    url = graphene.String(
        required=True,
        description='The URL of the file.'
    )

    class Meta:
        description = 'Represents an file.'

    def resolve_url(self, info):
        return self.url