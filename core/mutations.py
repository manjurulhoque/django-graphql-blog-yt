import graphene

from categories.mutations import CreateCategory, UpdateCategory, DeleteCategory
from posts.mutations import CreatePost, UpdatePost, DeletePost


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
