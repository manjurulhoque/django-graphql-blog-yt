import graphene

from categories.models import Category
from categories.object_types import CategoryType


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int(required=True))

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_category(self, info, id):
        return Category.objects.get(id=id)
