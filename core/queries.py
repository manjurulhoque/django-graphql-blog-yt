import graphene
from categories import queries as category_queries


class Query(category_queries.CategoryQuery, graphene.ObjectType):
    pass
