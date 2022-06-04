import graphene
from graphql import GraphQLError

from categories.forms import CategoryForm
from categories.models import Category


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, name):
        form = CategoryForm({"name": name})

        if form.is_valid():
            new_category = form.save()
            return CreateCategory(success=True)

        return CreateCategory(success=False)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, name):
        existing_category = Category.objects.get(id=id)
        try:
            existing_category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise GraphQLError("Category not found")

        form = CategoryForm({"name": name}, instance=existing_category)

        if form.is_valid():
            updated_category = form.save()
            return UpdateCategory(success=True)

        return UpdateCategory(success=False)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            existing_category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise GraphQLError("Category not found")

        if existing_category:
            existing_category.delete()
            return DeleteCategory(success=True)

        return DeleteCategory(success=False)
