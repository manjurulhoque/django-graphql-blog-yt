from graphene_django import DjangoObjectType

from posts.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
