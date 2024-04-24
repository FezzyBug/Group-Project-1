from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..controllers import reviews as controller
from ..schemas import reviews as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Reviews'],
    prefix="/reviews"
)


@router.post("/", response_model=schema.Reviews)
def create_reviews(request: schema.ReviewsCreate, db: Session = Depends(get_db)):
    """Create a new review."""
    return controller.create_review(db=db, request=request)


@router.get("/", response_model=List[schema.Reviews])
def read_all_reviews(db: Session = Depends(get_db)):
    """Read all reviews."""
    return controller.read_all_reviews(db)


@router.get("/{review_id}", response_model=schema.Reviews)
def read_review(review_id: int, db: Session = Depends(get_db)):
    """Read a review by ID."""
    return controller.read_review(db, review_id=review_id)


@router.put("/{review_id}", response_model=schema.Reviews)
def update_review(review_id: int, request: schema.ReviewsUpdate, db: Session = Depends(get_db)):
    """Update a review by ID."""
    return controller.update_review(db=db, request=request, review_id=review_id)


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    """Delete a review by ID."""
    return controller.delete_review(db=db, review_id=review_id)