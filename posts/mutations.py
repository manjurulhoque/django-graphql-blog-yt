import graphene
from graphql import GraphQLError

from posts.forms import PostForm


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
