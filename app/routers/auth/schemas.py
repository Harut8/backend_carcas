from typing import Annotated

from pydantic import BaseModel, ConfigDict, WrapValidator, validate_email
from pydantic_core import PydanticCustomError

from app.helpers.exceptions import ValidationError


def validate_email_format(error_class):
    def wrapper(value, handler):
        try:
            validate_email(value)
        except PydanticCustomError:
            raise error_class
        return value.lower()

    return wrapper


EmailString = Annotated[
    str,
    WrapValidator(validate_email_format(ValidationError("Invalid email format"))),
]


class UserPasswordSchema(BaseModel):
    email: EmailString
    password: str


class UserCreateSchema(UserPasswordSchema):
    phone: str
    name: str


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailString
    phone: str
    name: str


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
