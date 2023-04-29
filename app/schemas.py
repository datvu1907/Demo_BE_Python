from datetime import datetime
from pydantic import BaseModel, constr


class UserBaseSchema(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str


class LoginUserSchema(BaseModel):
    email: str
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema


class FlightBaseSchema(BaseModel):
    title: str
    description: str
    image: str
    price: int
    date: str

    class Config:
        orm_mode = True


class FlightResponseSchema(FlightBaseSchema):
    id: str
    pass


class FlightResponse(FlightResponseSchema):
    status: str
    data: FlightBaseSchema
