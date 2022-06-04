import graphene

from core.mutations import Mutation
from core.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
