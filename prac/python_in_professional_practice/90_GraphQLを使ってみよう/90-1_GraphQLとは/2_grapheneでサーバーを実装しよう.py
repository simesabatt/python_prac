from graphene import ObjectType, String, Schema


class MyQuery(ObjectType):
    hello = String(default_value='Hi!')


schema = Schema(query=MyQuery)
result = schema.execute('query { hello }')
print(result.data)