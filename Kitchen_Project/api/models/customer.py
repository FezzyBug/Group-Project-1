from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    phone = Column(String(20))
    address = Column(String(200))
    email = Column(String(100))
    password = Column(String(100))

    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")
