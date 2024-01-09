from graphene import ObjectType, String, Int, Field, Schema


class User(ObjectType):
    name = String()
    age = Int()


class MyQuery(ObjectType):
    current = Field(User)

    def resolve_current(parent, info):
        return User('Alice', 18)


schema = Schema(query=MyQuery)
result = schema.execute('{ current { name age } }')
print(result.data)


# {'current': {'name': 'Alice', 'age': 18}}