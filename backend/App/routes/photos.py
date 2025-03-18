from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import shutil, os
from App import crud, schemas, models
from App.dependencies import get_db

router = APIRouter()
UPLOAD_DIRECTORY = "uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/upload/", response_model=schemas.PhotoResponse)
def upload_photo(file: UploadFile = File(...), description: str = "", tags: str = "", db: Session = Depends(get_db)):
    file_path = f"{UPLOAD_DIRECTORY}{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_photo = crud.create_photo(db, schemas.PhotoCreate(filename=file.filename, description=description, tags=tags))
    return new_photo

@router.get("/photos/", response_model=list[schemas.PhotoResponse])
def list_photos(db: Session = Depends(get_db)):
    return crud.get_photos(db)

@router.delete("/photos/{photo_id}")
def delete_photo(photo_id: int, db: Session = Depends(get_db)):
    photo = crud.get_photo(db, photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    os.remove(f"{UPLOAD_DIRECTORY}{photo.filename}")
    crud.delete_photo(db, photo_id)
    return {"detail": "Photo deleted"}
