from datetime import datetime
from typing import Optional, Union, List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    username : str
    password : str
    email: str
    friends: List[int] = []
    active: Union[bool, None] = None
    signup_t: Optional[datetime] = None
    last_login: Optional[datetime] = None

class Users(BaseModel):
    users: List(User) # recursively use `Car`
    count: int

raw_user = {'id': 1,
            'name': 'Tim Doe',
            'username': 'timmy42',
            'password': 't#*12ajgEe',
            'email': 'timmy.42@yahoo.com',
            'friends': [],
            'active': None,
            'signup_t': '2023-10-01 12:42',
            'last_login':  '2023-10-13 18:08'
        }

structured_user = User(**raw_user)
print(structured_user.id)

external_data = {'id': 2, 'name': 'Jane Wu', 'username': 'jwuwu', 
                 'password': 'tata42', 'email': 'jane.wu@google.com',
                 'friends': [], 'active': None, 'signup_t': '2023-11-01 12:42',
                 'last_login':  '2023-11-13 18:08'
                 }