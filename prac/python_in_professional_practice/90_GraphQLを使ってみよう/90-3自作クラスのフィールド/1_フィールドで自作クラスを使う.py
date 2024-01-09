from graphene import ObjectType, String, Int, Field, Schema


class User(ObjectType):
    name = String()
    age = Int()


class MyQuery(ObjectType):
    current = Field(User)


schema = Schema(query=MyQuery)
result = schema.execute('{ current { name age } }')
print(result.data)