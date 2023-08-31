import json
from typing import Any

person = {'name': 'John', 'age': 34, 'city': 'Bosron'}

# personJSON = json.dumps(person, indent=4, separators=('; ','= '), sort_keys=True)
# with open('person.json','w') as file: json.dump(person, file, indent=5)

# personJSON = str(json.dumps(person))
# person = json.loads(personJSON)

# with open('person.json') as file:
#     person = json.load(file)
#     print(person)


class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


user = User('ali', 23)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User isnot JSON serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o) -> Any:
        if isinstance(o,User):
            return {'name':o.name,'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
    
# userJSON = json.dumps(user, default=encode_user)
# userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'] , age=dct['age'] )
    return dct

# user = json.loads(userJSON)
user = json.loads(userJSON, object_hook=decode_user)
print(user)