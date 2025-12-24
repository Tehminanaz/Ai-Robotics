# 12-Week Physical AI & Humanoid Robotics Course

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.4-green)](https://fastapi.tiangolo.com/)

Welcome to the comprehensive 12-Week Physical AI & Humanoid Robotics Course! This interactive learning platform combines educational content with AI-powered features to provide a personalized and engaging learning experience in robotics and artificial intelligence.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements a complete educational platform for Physical AI and Humanoid Robotics, featuring:
- Interactive textbook with 3 comprehensive modules
- Intelligent RAG (Retrieval Augmented Generation) chatbot
- Integration with OpenAI and Qdrant vector database
- Docusaurus-based frontend for course content
- FastAPI backend for content management and AI services

### Course Modules
1. **Module 1: Foundations of Physical AI** - Embodied AI, Robotics Fundamentals, ROS 2, Gazebo Simulation
2. **Module 2: Perception, Control, and Advanced Simulation** - Motor Control, Perception, Planning, NVIDIA Isaac Sim
3. **Module 3: Advanced AI, Humanoid Robotics, and Deployment** - RAG agents, Humanoid platforms, HRI, RL, Cloud Robotics

## Features

### 🧠 AI-Powered Learning Assistant
- Interactive chatbot for answering questions about course content
- Contextual Q&A based on selected text passages
- Conversation history tracking

### 🎯 Content Personalization
- **NEW**: Personalized content adaptation based on user background and experience
- Tailored explanations and examples relevant to your field of expertise
- Adaptive complexity matching your knowledge level

### 🌐 Multi-Language Support
- **NEW**: Real-time content translation to Urdu and other languages
- Preserves technical terminology and educational value
- Supports multiple languages: Urdu, Spanish, French, German, Chinese, Hindi, Arabic

### 📚 Interactive Content
- Rich course materials covering robotics fundamentals to advanced AI concepts
- Text highlighting functionality for contextual questioning
- Structured learning modules with practical examples

## Architecture

The application follows a modern microservices architecture:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │◄──►│   Backend API    │◄──►│  Vector DB      │
│   (Docusaurus)  │    │   (FastAPI)      │    │   (Qdrant)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                    ┌──────────────────┐
                    │   Content DB     │
                    │  (PostgreSQL)    │
                    └──────────────────┘
```

### Core Components

1. **Frontend (Docusaurus)**: Static site generation for course content
2. **Backend (FastAPI)**: RESTful API for content management and AI services
3. **Vector Database (Qdrant)**: Semantic search for RAG functionality
4. **Content Database (PostgreSQL)**: Persistent storage for course content
5. **AI Integration (OpenAI)**: LLM-powered question answering

## Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.9+)
- **Database**: PostgreSQL (NeonDB)
- **Vector Database**: Qdrant
- **AI/ML**: OpenAI API, LangChain, LangChain-OpenAI
- **Embeddings**: OpenAI text-embedding-ada-002
- **Text Processing**: LangChain Text Splitters

### Frontend
- **Framework**: Docusaurus (TypeScript/React)
- **Styling**: Tailwind CSS
- **UI Components**: Custom React components

### Development Tools
- **Python Package Management**: uv, pip-tools
- **Code Quality**: ESLint, Prettier, Black
- **Version Control**: Git

## Installation

### Prerequisites
- Python 3.9+
- Node.js 16+
- Access to OpenAI API
- Access to Qdrant Cloud (or local instance)

### Setup

1. **Clone the repository**:
```bash
git clone <repository-url>
cd <repository-name>
```

2. **Set up Python environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Set up Node.js environment**:
```bash
cd frontend
npm install
```

4. **Configure environment variables** (see [Environment Variables](#environment-variables) section)

5. **Install additional Python dependencies**:
```bash
pip install langchain-text-splitters
```

## Usage

### Running the Backend
```bash
cd /path/to/project
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

### Running the Frontend
```bash
cd frontend
npm start
```

The frontend will be available at `http://localhost:3000`

### API Endpoints

#### Backend API
- `GET /health` - Health check
- `POST /ingest` - Content ingestion endpoint
- `GET /check_db` - Database connection check
- `GET /check_qdrant` - Qdrant connection check

#### Frontend
- `/` - Main course landing page
- `/module1/*` - Module 1 content
- `/module2/*` - Module 2 content
- `/module3/*` - Module 3 content

### Personalization API (`/api/v1/personalization/`)
- `POST /personalize` - Personalize content based on user background
- `POST /translate` - Translate content to target languages

## Project Structure

```
.
├── backend/                  # Legacy FastAPI backend
├── frontend/                 # Docusaurus frontend
│   ├── docs/                 # Course content
│   │   ├── module1/          # Module 1 chapters
│   │   ├── module2/          # Module 2 chapters
│   │   └── module3/          # Module 3 chapters
│   ├── src/                  # Custom React components
│   └── docusaurus.config.ts  # Docusaurus configuration
├── src/                      # Main application source
│   ├── api/                  # API routes
│   ├── data/                 # Data models and database
│   ├── embeddings/           # Embedding generation
│   ├── ingestion/            # Content ingestion pipeline
│   ├── services/             # Business logic
│   └── main.py               # Application entry point
├── specs/                    # Specification documents
│   └── 003-physical-ai-course/ # Course specifications
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## API Endpoints

### Content Ingestion API
- `POST /ingest` - Ingest content for RAG system
  - Request body: `{"source_url": string, "text_content": string, "content_metadata": object}`
  - Response: `{"status": string, "content_id": uuid, "message": string}`

### Health Checks
- `GET /health` - Application health check
- `GET /check_db` - Database connectivity check
- `GET /check_qdrant` - Qdrant connectivity check

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Qdrant Configuration
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key

# Database Configuration
DATABASE_URL=your_postgresql_connection_string
```

### Environment Variables Explained

- `OPENAI_API_KEY`: API key for OpenAI services (for embeddings and LLM)
- `QDRANT_URL`: URL for Qdrant vector database instance
- `QDRANT_API_KEY`: API key for Qdrant instance
- `DATABASE_URL`: PostgreSQL connection string

## Development

### Adding New Course Content
1. Create new markdown files in `frontend/src/docs/moduleX/`
2. Update `_category_.json` in the respective module directory
3. Add content following the existing format

### Extending the RAG System
1. Modify ingestion pipeline in `src/ingestion/ingestion_pipeline.py`
2. Update RAG service in `src/services/rag_service.py`
3. Add new API endpoints in `src/api/`

### Frontend Customization
1. Add new components in `frontend/src/components/`
2. Modify Docusaurus configuration in `frontend/docusaurus.config.ts`
3. Update styling in `frontend/src/css/`

## 🤖 AI Features Explained

### Retrieval-Augmented Generation (RAG)
The system uses RAG to provide contextually relevant answers by retrieving relevant document chunks from the vector database and passing them to the LLM.

### Personalization Engine
Leverages GPT-4o to adapt content based on user's background, experience level, and interests, making learning more engaging and accessible.

### Multilingual Support
Advanced translation capabilities using GPT-4o to provide course content in multiple languages while preserving technical accuracy.

### Using the New Features

#### Content Personalization
Personalize course content to match your background and learning style:

```bash
curl -X POST "http://localhost:8000/api/v1/personalization/personalize" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Robots are machines that can perform tasks automatically...",
    "user_background": "I am a computer science student with knowledge of programming but new to robotics.",
    "chapter_title": "Introduction to Robotics"
  }'
```

#### Content Translation
Translate course content to Urdu or other supported languages:

```bash
curl -X POST "http://localhost:8000/api/v1/personalization/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Robots are machines that can perform tasks automatically...",
    "target_language": "ur"
  }'
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code Standards
- Python: Follow PEP 8 guidelines
- JavaScript/TypeScript: Use ESLint and Prettier
- Documentation: Update relevant documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the language models
- Qdrant for vector database services
- Docusaurus team for the documentation platform
- FastAPI team for the web framework

## Support

For support, please open an issue in the repository or contact the maintainers.