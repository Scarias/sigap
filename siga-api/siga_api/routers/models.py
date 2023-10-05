from pydantic import BaseModel


class User(BaseModel):
    username: str
    domain: str
    password: str
