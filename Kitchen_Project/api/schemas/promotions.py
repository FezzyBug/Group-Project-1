from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promo_code: str
    usage_limit: int
    applicable_items: str
    expiration_date: datetime


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    usage_limit: Optional[int] = None
    applicable_items: Optional[str] = None
    expiration_date: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True
