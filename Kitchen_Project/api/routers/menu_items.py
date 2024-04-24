from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menuitems"
)


@router.post("/", response_model=schema.MenuItems)
def create_promotion(request: schema.MenuItemsCreate, db: Session = Depends(get_db)):
    """Create a new promotion."""
    return controller.create_menuitem(db=db, request=request)


@router.get("/", response_model=List[schema.MenuItems])
def read_all_promotions(db: Session = Depends(get_db)):
    """Read all promotions."""
    return controller.read_all_menuitems(db)


@router.get("/{promotion_id}", response_model=schema.MenuItems)
def read_promotion(menuitem_id: int, db: Session = Depends(get_db)):
    """Read a promotion by ID."""
    return controller.read_menuitem(db, menuitem_id=menuitem_id)


@router.put("/{promotion_id}", response_model=schema.MenuItems)
def update_promotion(menuitem_id: int, request: schema.MenuItemsUpdate, db: Session = Depends(get_db)):
    """Update a promotion by ID."""
    return controller.update_menuitem(db=db, request=request, menuitem_id=menuitem_id)


@router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotion(menuitem_id: int, db: Session = Depends(get_db)):
    """Delete a promotion by ID."""
    return controller.delete_menuitem(db=db, menuitem_id=menuitem_id)
