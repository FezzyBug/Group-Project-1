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
def create_menuitems(request: schema.MenuItemsCreate, db: Session = Depends(get_db)):
    """Create a new menu item."""
    return controller.create_menuitem(db=db, request=request)


@router.get("/", response_model=List[schema.MenuItems])
def read_all_menuitems(db: Session = Depends(get_db)):
    """Read all menu itemss."""
    return controller.read_all_menuitems(db)


@router.get("/{menuitem_id}", response_model=schema.MenuItems)
def read_menuitem(menuitem_id: int, db: Session = Depends(get_db)):
    """Read a menu item by ID."""
    return controller.read_menuitem(db, menuitem_id=menuitem_id)


@router.put("/{menuitem_id}", response_model=schema.MenuItems)
def update_menuitem(menuitem_id: int, request: schema.MenuItemsUpdate, db: Session = Depends(get_db)):
    """Update a menu item by ID."""
    return controller.update_menuitem(db=db, request=request, menuitem_id=menuitem_id)


@router.delete("/{menuitem_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menuitem(menuitem_id: int, db: Session = Depends(get_db)):
    """Delete a menu item by ID."""
    return controller.delete_menuitem(db=db, menuitem_id=menuitem_id)
