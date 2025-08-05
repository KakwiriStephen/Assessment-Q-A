# AskAtlas - AI-Powered Q&A Assistant 🌍💬

An interactive modern web application built with FastAPI and Next.js that integrates a Language Learning Model (LLM) to provide intelligent, structured answers to user queries in real-time. Built with attention to clean code, responsiveness, and a delightful user experience.

---

## 📌 Project Overview

**AskAtlas** is a full-stack AI-powered Q&A assistant that allows users to input natural language questions and receive real-time, structured responses from a powerful LLM (DeepSeek-V3 via Hugging Face). The app is responsive, clean, and designed for real-world AI assistant use cases like travel guidance, general information, and more.

---

## 🚀 Tech Stack

| Layer        | Technology           |
| ------------ | -------------------- |
| **Frontend** | Next.js (App Router) |
| **Styling**  | TailwindCSS          |
| **Backend**  | FastAPI (Python 3.11) |
| **LLM**      | DeepSeek-V3 (via Hugging Face) |
| **Deployments** | Vercel (Frontend), Railway/Render (Backend) |

---

## 🛠️ Setup Instructions

### Prerequisites
- Node.js (v16 or later)
- Python 3.11+
- npm or yarn
- Hugging Face API token

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (see [Environment Variables](#-environment-variables) section)

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

### Running Locally
1. Start the backend server (from the backend directory):
   ```bash
   uvicorn main:app --reload
   ```
2. Start the frontend development server (from the frontend directory):
   ```bash
   npm run dev
   # or
   yarn dev
   ```
3. Open [http://localhost:3000](http://localhost:3000) in your browser

---

## 🤖 LLM Prompts

The application uses the following prompt structure for the LLM:

### System Prompt
```
You are a travel documentation assistant. Answer the following question in a helpful, organized format.
```

### User Prompt Structure
```
Question: "[user's question]"
```

The LLM is configured to provide well-structured, detailed responses with proper formatting for better readability.

## 📂 Folder Structure

```
AskAtlas/
├── backend/               # FastAPI backend
│   ├── main.py           # Main FastAPI app
│   ├── llm.py            # LLM interaction logic
│   ├── config.py         # Environment configuration
│   └── prompt_utils.py   # Prompt formatting helper
└── frontend/             # Next.js frontend
    ├── src/
    │   ├── app/         # App router
    │   ├── components/   # Reusable components
    │   └── utils/       # Utility functions
    ├── public/          # Static files
    └── package.json     # Frontend dependencies
```

---

## 🔐 Environment Variables

Create a `.env` file in the `backend` directory with the following variables:

```
# Backend Configuration
HF_TOKEN=your_huggingface_token_here
ALLOWED_ORIGINS=http://localhost:3000
```

### Environment Variables Explained
- `HF_TOKEN`: Your Hugging Face API token for accessing the DeepSeek-V3 model
- `ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins (default: http://localhost:3000)

---

## 🚀 Deployment

### Backend Deployment
1. Deploy the FastAPI backend to a service like Railway or Render
2. Set up the environment variables in your deployment environment
3. Configure the frontend to point to your backend URL

### Frontend Deployment
1. Build the production version:
   ```bash
   npm run build
   # or
   yarn build
   ```
2. Deploy to Vercel or your preferred static hosting service

---

## 📝 License

MIT
ANTHROPIC_API_KEY=your_anthropic_api_key
ALLOWED_ORIGINS=http://localhost:3000
```

---

## 🛠️ Setup Instructions

### 📦 Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn main:app --reload
```
The FastAPI server will be running at http://127.0.0.1:8000.

Test the /ask endpoint via Swagger UI:
➡️ http://127.0.0.1:8000/docs

### 🌐 Frontend (Next.js + TailwindCSS)
```bash
cd frontend
npm install
npm run dev
```
The app will run at http://localhost:3000.

---

## 📤 API Endpoint

**POST /ask**

Request Body:
```json
{
  "question": "What do I need to travel from Kenya to Ireland?"
}
```
Response:
```json
{
  "answer": "To travel from Kenya to Ireland, you need a valid visa, a passport..."
}
```

---

## ✨ Features
- Ask questions in natural language
- Real-time LLM-powered responses
- Responsive modern UI
- Input validation & error handling
- Clean folder structure
- Prompt formatting abstraction
- (Bonus) Query history (optional)

---

## 🧪 Prompt Engineering Strategy
Prompts sent to the LLM are carefully formatted to guide the AI toward structured, clear answers. For example:

```
You are a travel documentation assistant. Answer the following question in a helpful, organized format:

Question: "What do I need to travel from Kenya to Ireland?"
```

---

## 🌐 Deployment

### Frontend (Optional Bonus)
Deploy via Vercel
```bash
vercel --prod
```

### Backend (Optional Bonus)
Deploy via Render or Railway

---

## 📎 Sample Prompts for Testing
- "What are the requirements to study in Canada?"
- "What documents do I need to visit South Africa from India?"
- "How can I register a business in Kenya?"

---

## ✅ Assessment Checklist
- Responsive frontend (Next.js + TailwindCSS)
- Backend API (FastAPI)
- LLM integration using Claude Sonnet 3.7 (Anthropic API)
- Prompt documentation
- Input/output structure and error handling
- .env template and setup instructions
- GitHub repo with all files
- (Optional) Deployed frontend/backend

---
