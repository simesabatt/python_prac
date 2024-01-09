import json

# JSON形式の文字列を定義
person_str_as_json = '{"id": 101, "name": "古村健太郎", "age": 38}'

# JSON形式の文字列をPythonの型（辞書）に変換
person = json.loads(person_str_as_json)


print(f'{person["name"]} {person["age"]}歳')