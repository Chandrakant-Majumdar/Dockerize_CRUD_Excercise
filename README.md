
# FastAPI Student CRUD API (Dockerized)

A FastAPI application for managing student records with full CRUD (Create, Read, Update, Delete) operations. The project is fully containerized and published to Docker Hub for easy deployment anywhere.

---

## 🚀 Run Anywhere with Docker

You can run this application on **any platform** (Windows, macOS, Linux) using Docker. No need to install Python or dependencies manually!

### 1. Pull the Docker Image from Docker Hub

```bash
docker pull chandrka54/dockerize-crud-excercise:latest
```

### 2. Run the Docker Container

```bash
docker run -d -p 8000:8000 chandrka54/dockerize-crud-excercise:latest
```

- The API will be available at [http://localhost:8000](http://localhost:8000)
- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

#### Notes
- Make sure Docker is installed and running on your system.
- This image is already pushed to Docker Hub and can be run anywhere with Docker support.
- For custom builds, you can use the provided Dockerfile:

```bash
docker build -t yourname/fastapi-crud-exercise .
docker run -d -p 8000:8000 yourname/fastapi-crud-exercise
```

---

## 🐳 How I Pushed the Image to Docker Hub

1. **Log in to Docker Hub:**
   ```bash
   docker login
   ```
2. **Build the Docker image:**
   ```bash
   docker build -t chandrka54/dockerize-crud-excercise:latest .
   ```
3. **Push the image to Docker Hub:**
   ```bash
   docker push chandrka54/dockerize-crud-excercise:latest
   ```

---

## 📝 API Endpoints

| Method | Endpoint                 | Description                   |
| ------ | ------------------------ | ----------------------------- |
| POST   | `/students/{student_id}` | Create a new student          |
| GET    | `/students/{student_id}` | Retrieve student by ID        |
| PUT    | `/students/{student_id}` | Update student information    |
| DELETE | `/students/{student_id}` | Delete student by ID          |
| GET    | `/`                      | View API overview and author  |

---

## 📦 Project Structure

```
Dockerize_fastAPI_CRUD_Excercise/
├── Dockerfile
├── main.py
├── requirments.txt
├── .env
├── .gitignore
├── .dockerignore
├── app/
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── routes.py
│   ├── api/
│   │   └── routes.py
│   ├── models/
│   │   └── student.py
│   ├── schemas/
│   │   └── student.py
│   └── services/
│       └── student_service.py
```

---

## 📁 Important Files

### .gitignore
Specifies files and folders to be ignored by git version control. Example:
```
__pycache__/
*.pyc
venv/
.env
.DS_Store
```

### .env
Environment variables for sensitive or environment-specific settings. Example:
```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
DEBUG=True
```

### .dockerignore
Files and folders to exclude from the Docker build context. Example:
```
__pycache__/
*.pyc
venv/
.git
.gitignore
.env
.DS_Store
```

---

## 🛠️ Local Development (Optional)

If you want to run the app locally (without Docker):

1. Clone the repository:
   ```bash
   git clone https://github.com/Chandrakant-Majumdar/fastAPI_CRUD_Excercise.git
   cd fastAPI_CRUD_Excercise/Dockerize_fastAPI_CRUD_Excercise
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirments.txt
   ```
4. Run the application:
   ```bash
   fastapi dev main.py
   # or
   uvicorn main:app --reload
   ```

---

## 👤 Author

Developed by **Chandrakant Majumdar**

---

