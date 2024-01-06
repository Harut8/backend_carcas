from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.helpers.db import BaseModel


class User(BaseModel):
    name: Mapped[str]
    email: Mapped[str]
    products: Mapped[list["Product"] | None] = relationship(back_populates="user")


class Product(BaseModel):
    name: Mapped[str]
    price: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User | None] = relationship(back_populates="products")


class Order(BaseModel):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
