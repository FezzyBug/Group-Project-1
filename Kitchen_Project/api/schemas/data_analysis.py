from typing import Optional
from pydantic import BaseModel


class DataAnalysisBase(BaseModel):
    sale_id: int
    order_id: int
    order_date: str
    item_id: int
    profit_margin: float
    quantity: int


class DataAnalysisCreate(DataAnalysisBase):
    pass


class DataAnalysisUpdate(BaseModel):
    sale_id: Optional[int] = None
    order_id: Optional[int] = None
    order_date: Optional[str] = None
    item_id: Optional[int] = None
    profit_margin: Optional[float] = None
    quantity: Optional[int] = None


class DataAnalysis(DataAnalysisBase):

    id = int

    class Config:
        orm_mode = True
