from fastapi import FastAPI, File, UploadFile, Query
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the upload folder
UPLOAD_FOLDER = "uploads"
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

# Serve static files (uploaded images)
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")

# API to upload photos
@app.post("/api/photos/")
async def upload_photo(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "Photo uploaded successfully",
        "filename": file.filename,
        "url": f"/uploads/{file.filename}"
    }

# API to get all uploaded photos
@app.get("/api/photos/")
def get_uploaded_photos():
    photos = [
        {"id": idx, "src": f"/uploads/{filename}", "title": filename}
        for idx, filename in enumerate(os.listdir(UPLOAD_FOLDER))
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, filename))
    ]
    return {"photos": photos}

# API to search photos by filename
@app.get("/api/search/")
def search_photos(query: str = Query(..., min_length=1)):
    results = [
        {"id": idx, "src": f"/uploads/{filename}", "title": filename}
        for idx, filename in enumerate(os.listdir(UPLOAD_FOLDER))
        if query.lower() in filename.lower()
    ]
    return {"photos": results}
