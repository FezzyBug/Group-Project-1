from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100))
    description = Column(String(300))
    price = Column(DECIMAL)
    ingredients = Column(Text)
    category = Column(String(50))
