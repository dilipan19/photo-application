📸 Photo Library Application

A modern, user-friendly photo management app built with React (frontend) and FastAPI (backend).


🚀 Features

✅ Upload Photos – Users can upload images with descriptions and tags.

✅ Organize Albums – Photos are stored in different albums.

✅ Search & Filter – Users can search photos based on tags or descriptions.

✅ View & Manage Photos – Delete or edit uploaded photos.

✅ Breadcrumb Navigation – Easy navigation between pages.

🛠️ Tech Stack

Frontend:

React.js

Bootstrap (for styling)

Axios (for API requests)

React Router (for navigation)

Backend:

FastAPI (Python)

Uvicorn (for server)

Pydantic (for validation)

CORS Middleware (to allow frontend requests)

Database:
SQLite (for storing metadata)

File System (for storing images)

📂 Folder Structure

📦 Photo-Library-App

 ┣ 📂 backend
 
 ┃ ┣ 📜 main.py          # FastAPI Backend
 
 ┃ ┣ 📜 models.py        # Database Models
 
 ┃ ┣ 📜 routes.py        # API Routes
 
 ┃ ┣ 📜 database.py      # Database Connection
 
 ┣ 📂 frontend
 
 ┃ ┣ 📂 src
 
 ┃ ┃ ┣ 📂 components
 
 ┃ ┃ ┃ ┣ 📜 UploadPhoto.jsx      # Upload UI
 
 ┃ ┃ ┃ ┣ 📜 DisplayPhotos.jsx    # Display UI

 
 ┃ ┃ ┃ ┣ 📜 SearchPhotos.jsx     # Search Functionality
 
 ┃ ┃ ┣ 📜 App.js         # Main React App
 
 ┃ ┃ ┣ 📜 index.js       # React Root
 
 ┃ ┃ ┣ 📜 styles.css     # Global CSS
 
 ┃ ┣ 📜 package.json     # React Dependencies
 
 ┣ 📜 README.md
 
 ┣ 📜 requirements.txt   # Backend Dependencies
 
 ┣ 📜 .gitignore         # Ignore files
 
🎯 Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/yourusername/photo-library-app.git

cd photo-library-app

2️⃣ Install Backend Dependencies

cd backend

pip install -r requirements.txt

3️⃣ Run the Backend Server

uvicorn main:app --reload

Your API will run at: http://127.0.0.1:8000

4️⃣ Install Frontend Dependencies

cd frontend

npm install

5️⃣ Start the React App
bash
Copy
Edit
npm start
Your app will be available at: http://localhost:3000

🎨 Screenshots

![Screenshot 2025-03-18 115001](https://github.com/user-attachments/assets/d8a87150-e8bb-4cc0-8a52-d3c736879817)


![Screenshot 2025-03-18 115114](https://github.com/user-attachments/assets/b56d7aab-d51f-4480-a146-f16e52aae977)



![Screenshot 2025-03-18 115131](https://github.com/user-attachments/assets/6eb40023-aa9a-41f6-a992-e6b93ae97b0d)


📢 API Endpoints

Method	Endpoint	Description

POST	/api/photos/	Upload a new photo

GET	/api/photos/{album}	Get photos from an album

GET	/api/search?query=	Search photos

DELETE	/api/photos/{id}	Delete a photo

🏆 Extra Features (Future Updates)

✔ AI-based Tagging








