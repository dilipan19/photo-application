from pydantic import BaseModel
from typing import Optional, List

class PhotoBase(BaseModel):
    description: Optional[str] = None
    tags: Optional[str] = None
    directory_id: Optional[int] = None

class PhotoCreate(PhotoBase):
    filename: str

class PhotoResponse(PhotoBase):
    id: int
    filename: str

class DirectoryBase(BaseModel):
    name: str

class DirectoryResponse(DirectoryBase):
    id: int
