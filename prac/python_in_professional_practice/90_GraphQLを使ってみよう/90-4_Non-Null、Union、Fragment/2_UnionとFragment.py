from graphene import ObjectType, String, Union, List, Schema


class User(ObjectType):
    name = String()


class Company(ObjectType):
    name = String()


class SearchResult(Union):
    class Meta:
        types = User, Company


class Query(ObjectType):
    result = [User('Daikichi'), Company('Kaisha')]
    search = List(SearchResult, q=String(),
                  default_value=result)


schema = Schema(Query)
result = schema.execute("""{
   search(q: "ai") {
       ... on User { name }
       ... on Company { name }
   }
}""")
print(result.to_dict())