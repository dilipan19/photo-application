from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from App import models
from App.dependencies import get_db

router = APIRouter()

@router.get("/search/")

def search_photos(query: str, db: Session = Depends(get_db)):
    return db.query(models.Photo).filter((models.Photo.tags.contains(query)) | (models.Photo.description.contains(query))).all()
