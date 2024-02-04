from pydantic import BaseModel, Field
from datetime import date


class UserIn(BaseModel):
    name: str = Field(min_length=2)
    surname: str = Field(min_length=2)
    birthday: date
    email: str
    address: str = Field(min_length=5)


class UserOut(UserIn):
    id: int
