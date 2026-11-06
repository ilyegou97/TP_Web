from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str



user = User(id=1, name="Sacha", age=10, email="sacha@pokemon.com")
print(user)


user2 = User(id=2, name="Ondine", age="25", email="ondine@pokemon.com")
print(user2.age, type(user2.age))


try:
    User(id="abc", name="Pierre", age=15)
except ValidationError as e:
    print(e)
