from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(50))
    usage_limit = Column(Integer)
    applicable_items = Column(String(200))
    expiration_date = Column(DATETIME)
