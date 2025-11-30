# Quickstart Guide: Physical AI Course Website

This guide provides a quick overview of how to set up and run the Physical AI Course Website project locally.

## 1. Environment Setup

### Prerequisites
- **Python 3.11+**: For the FastAPI backend.
- **Node.js LTS**: For the Docusaurus frontend (comes with npm).
- **Git**: For version control.
- **Docker / Docker Compose**: (Recommended) For running Neon Postgres and Qdrant locally.

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/physical-ai-course.git
    cd physical-ai-course
    ```
2.  **Create a virtual environment for Python backend**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

## 2. Backend Setup (FastAPI)

### Dependencies
1.  **Install Python dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    ```
    *(Note: `backend/requirements.txt` needs to be created with FastAPI, Uvicorn, Neon DB client, Qdrant client, Better-Auth libs, etc.)*

### Database Setup (Neon Postgres & Qdrant)

*(Assuming Docker Compose setup:)*

1.  **Start database services**:
    ```bash
    docker-compose up -d postgres qdrant
    ```
    *(Note: `docker-compose.yml` needs to be created for Postgres and Qdrant services.)*

2.  **Environment Variables**: Create a `.env` file in the `backend/` directory based on `backend/.env.example` (which needs to be created).
    ```ini
    # backend/.env
    DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
    QDRANT_HOST="localhost"
    QDRANT_PORT="6333"
    OPENAI_API_KEY="your_openai_api_key"
    AUTH_SECRET_KEY="your_auth_secret_key"
    # ... other backend specific env vars
    ```

### Run the Backend
```bash
cd backend
uvicorn src.main:app --reload
```
(Assumes `src/main.py` is the entry point for your FastAPI app)

## 3. Frontend Setup (Docusaurus)

### Dependencies
1.  **Install Node.js dependencies**:
    ```bash
    cd frontend
    npm install
    ```

### Run the Frontend
```bash
npm start
```
This will open the Docusaurus website in your browser (usually at `http://localhost:3000`).

## 4. Initial Content & Embeddings

*(Details for populating initial course content and generating Qdrant embeddings will be covered in more advanced guides. This typically involves a script to process markdown files and push them to Qdrant.)*