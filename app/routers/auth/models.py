from sqlalchemy.orm import Mapped

from app.helpers.db import BaseModel


class User(BaseModel):
    email: Mapped[str]
    password: Mapped[str]
    phone: Mapped[str]
    name: Mapped[str]
