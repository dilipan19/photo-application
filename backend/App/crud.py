from sqlalchemy.orm import Session
from . import models, schemas

def create_photo(db: Session, photo: schemas.PhotoCreate):
    db_photo = models.Photo(**photo.dict())
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

def get_photos(db: Session):
    return db.query(models.Photo).all()

def get_photo(db: Session, photo_id: int):
    return db.query(models.Photo).filter(models.Photo.id == photo_id).first()

def delete_photo(db: Session, photo_id: int):
    db_photo = get_photo(db, photo_id)
    if db_photo:
        db.delete(db_photo)
        db.commit()
    return db_photo
