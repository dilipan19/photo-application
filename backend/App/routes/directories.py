from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from App import schemas, models
from App.dependencies import get_db

router = APIRouter()

@router.post("/directories/", response_model=schemas.DirectoryResponse)
def create_directory(name: str, db: Session = Depends(get_db)):
    directory = models.Directory(name=name)
    db.add(directory)
    db.commit()
    db.refresh(directory)
    return directory

@router.get("/directories/", response_model=list[schemas.DirectoryResponse])
def list_directories(db: Session = Depends(get_db)):
    return db.query(models.Directory).all()
