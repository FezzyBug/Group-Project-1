from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    rating = Column(Integer)
    feedback = Column(Text)

    customer = relationship("Customer", back_populates="reviews")
    order = relationship("Order", back_populates="review")
