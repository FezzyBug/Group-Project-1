from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)


@router.post("/", response_model=schema.Promotion)
def create_promotion(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    """Create a new promotion."""
    return controller.create_promotion(db=db, request=request)


@router.get("/", response_model=List[schema.Promotion])
def read_all_promotions(db: Session = Depends(get_db)):
    """Read all promotions."""
    return controller.read_all_promotions(db)


@router.get("/{promotion_id}", response_model=schema.Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    """Read a promotion by ID."""
    return controller.read_promotion(db, promotion_id=promotion_id)


@router.put("/{promotion_id}", response_model=schema.Promotion)
def update_promotion(promotion_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    """Update a promotion by ID."""
    return controller.update_promotion(db=db, request=request, promotion_id=promotion_id)


@router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    """Delete a promotion by ID."""
    return controller.delete_promotion(db=db, promotion_id=promotion_id)
