from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Integer, Text


class ReviewsBase(BaseModel):
    customer_id: Integer
    order_id: Integer
    rating: Integer
    feedback: Text


class ReviewsCreate(ReviewsBase):
    pass


class ReviewsUpdate(BaseModel):
    customer_id: Optional[Integer] = None
    order_id: Optional[Integer] = None
    rating: Optional[Integer] = None
    feedback: Optional[Text] = None


class Reviews(ReviewsBase):
    id: int

    class Config:
        orm_mode = True
