from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


john: Person = {"name": "John", "age": 18}
