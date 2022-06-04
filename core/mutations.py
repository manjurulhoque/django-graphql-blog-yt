import graphene

from categories.mutations import CreateCategory, UpdateCategory, DeleteCategory


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
