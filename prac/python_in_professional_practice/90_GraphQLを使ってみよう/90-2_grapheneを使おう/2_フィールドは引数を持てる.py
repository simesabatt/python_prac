from graphene import ObjectType, String, Schema


class MyQuery(ObjectType):

    hello = String(name=String(default_value='stranger'))
    def resolve_hello(parent, info, name):
        return f'Hi {name}!'

schema = Schema(query=MyQuery)
print(schema.execute('{ hello }').data)
print(schema.execute('{ hello(name: "Taro") }').data)
