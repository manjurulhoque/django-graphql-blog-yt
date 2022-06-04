import graphene
from graphql import GraphQLError

from posts.forms import PostForm
from posts.models import Post


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        category_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, title, content, category_id, **kwargs):
        form = PostForm({"title": title, "content": content, "category": category_id})
        if form.is_valid():
            new_post = form.save()
            return CreatePost(success=True)
        print(form.errors)
        return CreatePost(success=False)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        category_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, title, content, category_id, **kwargs):
        try:
            existing_post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise GraphQLError("Post not found")

        form = PostForm({"title": title, "content": content, "category": category_id}, instance=existing_post)
        if form.is_valid():
            updated_post = form.save()
            return UpdatePost(success=True)
        print(form.errors)
        return UpdatePost(success=False)
