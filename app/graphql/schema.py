import strawberry

from . import mutation, query

schema = strawberry.Schema(query=query.Query, mutation=mutation.Mutation)


# import strawberry
# from graphql import GraphQLError
# from strawberry.extensions import Extension
#
#
# class ExampleError(Exception):
#     pass
#
#
# class ExtendErrorFormat(Extension):
#     def on_request_end(self):
#         result = self.execution_context.result
#         if result.errors:
#             processed_errors = []
#             for error in result.errors:
#
#                 if error.original_error and isinstance(error.original_error, ExampleError):
#                     processed_errors.append(
#                         GraphQLError(
#                             extensions={"additional_key": "additional_value"},
#                             nodes=error.nodes,
#                             source=error.source,
#                             positions=error.positions,
#                             path=error.path,
#                             original_error=error.original_error,
#                             message=error.message,
#                         )
#                     )
#                 else:
#                     processed_errors.append(error)
#
#             result.errors = processed_errors
#
#
# @strawberry.type
# class Query:
#     @strawberry.field
#     def my_field(self) -> str:
#         raise ExampleError("This error format has 'additional_key' in extensions key")
#
#     @strawberry.field
#     def my_second_field(self) -> str:
#         raise Exception("This error has normal format")
#
#
# schema = strawberry.Schema(Query, extensions=[ExtendErrorFormat])
