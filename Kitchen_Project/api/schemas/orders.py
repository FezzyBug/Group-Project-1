from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail

# id = Column(Integer, primary_key=True, index=True, autoincrement=True)
# customer_name = Column(String(100))
# order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
# description = Column(String(300))
#
# order_details = relationship("OrderDetail", back_populates="order")


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
