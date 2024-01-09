from graphene import ObjectType, String, Schema


class MyQuery(ObjectType):
    hello = String()

    def resolve_hello(parent, info):
        return 'Hi!'


schema = Schema(query=MyQuery)
print(schema.execute('query { hello }').data)
print(schema.execute('query MyTest { hello }').data)
print(schema.execute('{ hello }').data)
print(schema.execute('{ new_label: hello }').data)