import graphene

from core.mutations import Mutation


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query, mutation=Mutation)
