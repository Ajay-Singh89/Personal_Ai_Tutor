# 🎓 Personal AI Tutor

An AI-powered personal tutoring application that allows students to interact with an AI tutor through a simple web-based chat interface.

The project uses a **JavaScript frontend**, **FastAPI backend**, **LangChain**, and **Google Gemini** to provide AI-powered conversational learning.

---

## 🚀 Features

* 💬 Interactive AI chat interface
* 🤖 AI-powered responses using Google Gemini
* 🔗 LangChain integration for LLM communication
* ⚡ FastAPI backend REST API
* 🌐 HTML, CSS, and JavaScript frontend
* 🔐 Environment variables for secure API key management
* 🧩 Modular agent architecture
* 📚 Designed to support personalized learning features
* 🔌 Frontend-backend communication using REST APIs

---

## 🏗️ Architecture

```text
                    PERSONAL AI TUTOR
                           │
                           ▼
                 ┌───────────────────┐
                 │     Frontend      │
                 │    HTML/CSS/JS    │
                 └─────────┬─────────┘
                           │
                       HTTP / JSON
                           │
                           ▼
                 ┌───────────────────┐
                 │      FastAPI      │
                 │      Backend      │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    Agent Module   │
                 │     LangChain     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Google Gemini   │
                 │       LLM         │
                 └─────────┬─────────┘
                           │
                           ▼
                      AI Response
                           │
                           ▼
                       Frontend
```

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

### AI

* LangChain
* Google Gemini

### Development Tools

* Git
* GitHub
* Python Virtual Environment

---

## 📁 Project Structure

```text
personal-ai-tutor/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   │
│   └── agent/
│       ├── __init__.py
│       └── agent.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. The student enters a question in the frontend chat interface.
2. JavaScript captures the student's message.
3. The frontend sends the message to the FastAPI `/chat` endpoint using an HTTP POST request.
4. FastAPI validates the incoming request.
5. The backend passes the message to the LangChain agent.
6. LangChain communicates with Google Gemini.
7. Gemini generates an AI response.
8. FastAPI returns the response as JSON.
9. JavaScript receives the response and displays it in the chat interface.

### Request Flow

```text
Student
   ↓
JavaScript
   ↓
POST /chat
   ↓
FastAPI
   ↓
LangChain Agent
   ↓
Google Gemini
   ↓
FastAPI
   ↓
JSON Response
   ↓
JavaScript
   ↓
Student
```

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/personal-ai-tutor.git
```

Navigate into the project:

```bash
cd personal-ai-tutor
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file containing your Google Gemini API key:

```text
GOOGLE_API_KEY=your_api_key_here
```

**Never commit your ****`.env`**** file to GitHub.**

The `.gitignore` file is configured to prevent environment files and sensitive credentials from being uploaded.

---

## ▶️ Running the Backend

Navigate to the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

---

## 🔌 API

### POST `/chat`

Sends a message to the AI tutor.

#### Request

```json
{
    "message": "Explain machine learning in simple terms."
}
```

#### Response

```json
{
    "response": "Machine learning is a branch of artificial intelligence..."
}
```

---

## 🔮 Future Improvements

The project is designed to evolve into a more advanced AI tutoring system with personalized learning capabilities.

### 🧠 AI & Agentic Features

* **RAG (Retrieval-Augmented Generation)** — Allow the tutor to retrieve relevant information from uploaded textbooks, lecture notes, PDFs, and other educational resources before generating answers.
* **Tool Calling** — Give the AI access to tools such as calculators, web search, and database queries.
* **AI Agent** — Enable the system to decide when to use different tools based on the student's question.
* **Conversation Memory** — Maintain context across multiple messages and conversations.
* **Multi-Agent Architecture** — Introduce specialized agents for teaching, quiz generation, evaluation, and research.

### 📚 Personalized Learning

* **Personalized Learning Paths** — Adapt explanations and learning material based on the student's knowledge level.
* **Student Profiles** — Store subjects, learning preferences, strengths, and weaknesses.
* **Learning History** — Track topics studied and previous interactions.
* **Progress Tracking** — Provide insights into the student's learning progress.
* **Adaptive Difficulty** — Automatically adjust question difficulty based on student performance.

### 📝 Educational Features

* **AI-Generated Quizzes** — Generate quizzes based on the student's current topic.
* **Automatic Answer Evaluation** — Evaluate student answers and explain mistakes.
* **Practice Tests** — Generate topic-specific tests with scoring.
* **Flashcard Generation** — Automatically create flashcards from notes or uploaded documents.
* **Study Plan Generation** — Create personalized study plans based on subjects and deadlines.

### 🗄️ Backend & Infrastructure

* **Database Integration** — Store users, conversations, learning history, quiz results, and progress.
* **User Authentication** — Add secure registration and login functionality.
* **Vector Database** — Store document embeddings for efficient RAG-based retrieval.
* **Document Processing Pipeline** — Support uploading and processing PDFs and educational documents.
* **Streaming Responses** — Stream AI responses to the frontend for a more interactive experience.
* **Cloud Deployment** — Deploy the application to cloud infrastructure.

---

## 🔎 Planned RAG Pipeline

A future RAG implementation will allow students to upload their own learning material and ask questions about it.

```text
                    Student Question
                           ↓
                       Frontend
                           ↓
                        FastAPI
                           ↓
                    RAG Pipeline
                           ↓
                    Query Embedding
                           ↓
                    Vector Database
                           ↓
               Retrieve Relevant Documents
                           ↓
                    Relevant Context
                           ↓
                     Gemini LLM
                           ↓
                    AI Tutor Response
                           ↓
                       Frontend
```

The document ingestion pipeline would work approximately as follows:

```text
PDF / Notes
    ↓
Document Loader
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Semantic Search
    ↓
Relevant Context
    ↓
Gemini
```

This will allow the tutor to provide answers grounded in **student-provided educational material**.

---

## 🎯 Learning Objectives

This project is designed to provide practical experience with:

* Building REST APIs
* Frontend-backend communication
* FastAPI application development
* LLM integration
* LangChain
* AI agent architecture
* Prompt engineering
* Environment variable management
* Git and GitHub
* RAG architecture
* Database integration
* AI-powered educational applications

---

## 🚧 Project Status

**Current Status:** 🟢 Initial Development

### Currently Implemented

* [x] HTML/CSS/JavaScript chat interface
* [x] FastAPI backend
* [x] REST API communication
* [x] LangChain integration
* [x] Google Gemini integration
* [x] Modular agent structure
* [x] Environment variable configuration

### Planned

* [ ] Conversation memory
* [ ] Database integration
* [ ] RAG
* [ ] Vector database
* [ ] Document upload
* [ ] AI-generated quizzes
* [ ] Automatic answer evaluation
* [ ] Student progress tracking
* [ ] Authentication
* [ ] AI tools and function calling
* [ ] Cloud deployment

---

## 👨‍💻 Author

**Ajay Singh**

Built as a portfolio project focused on **Python, FastAPI, LangChain, LLMs, and Agentic AI**.
