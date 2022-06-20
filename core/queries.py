import graphene
from categories import queries as category_queries
from posts import queries as post_queries


class Query(category_queries.CategoryQuery, post_queries.PostQuery, graphene.ObjectType):
    pass
