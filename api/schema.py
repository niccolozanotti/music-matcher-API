import strawberry

from .query import Query
from .mutation import Mutation

# Note: strawberry automatically includes types usedy by any resolver
schema = strawberry.Schema(query=Query, mutation=Mutation)