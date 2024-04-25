from fastapi import APIRouter, Depends, status, FastAPI, Response
from sqlalchemy.orm import Session
from typing import List
from ..controllers import data_analysis as controller
from ..schemas import data_analysis as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Data Analysis'],
    prefix="/dataanalysis"
)


@router.post("/", response_model=schema.DataAnalysis)
def create_data_analysis(request: schema.DataAnalysisCreate, db: Session = Depends(get_db)):
    """Create a new data analysis entry."""
    return controller.create_data_analysis(db=db, request=request)


@router.get("/", response_model=List[schema.DataAnalysis])
def read_all_dataanalysis(db: Session = Depends(get_db)):
    """Read all data analysis entries."""
    return controller.read_all_data_analysis(db)


@router.get("/{data_analysis_id}", response_model=schema.DataAnalysis)
def read_data_analysis(data_analysis_id: int, db: Session = Depends(get_db)):
    """Read data analysis by ID."""
    return controller.read_data_analysis(db, data_analysis_id=data_analysis_id)


@router.put("/{data_analysis_id}", response_model=schema.DataAnalysis)
def update_data_analysis(data_analysis_id: int, request: schema.DataAnalysisUpdate, db: Session = Depends(get_db)):
    """Update data analysis by ID."""
    return controller.update_data_analysis(db=db, request=request, data_analysis_id=data_analysis_id)


@router.delete("/{data_analysis_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_data_analysis(data_analysis_id: int, db: Session = Depends(get_db)):
    """Delete data analysis by ID."""
    return controller.delete_data_analysis(db=db, data_analysis_id=data_analysis_id)
