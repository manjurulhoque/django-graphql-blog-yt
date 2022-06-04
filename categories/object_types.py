from graphene_django import DjangoObjectType

from categories.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
