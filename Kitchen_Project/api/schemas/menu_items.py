from typing import Optional
from pydantic import BaseModel
from sqlalchemy import DECIMAL, Text


class MenuItemsBase(BaseModel):
    dish_name: str
    description: str
    price: DECIMAL
    ingredients: Text
    category: str


class MenuItemsCreate(MenuItemsBase):
    pass


class MenuItemsUpdate(BaseModel):
    dish_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[DECIMAL] = None
    ingredients: Optional[Text] = None
    category: Optional[str] = None


class MenuItems(MenuItemsBase):
    id: int

    class Config:
        orm_mode = True
