from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class DataAnalysis(Base):
    __tablename__ = 'data_analysis'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    date = Column(DATETIME, default=datetime.now)
    item_id = Column(Integer, ForeignKey('menu_items.id'))
    profit_margin = Column(DECIMAL)
    quantity = Column(Integer)
