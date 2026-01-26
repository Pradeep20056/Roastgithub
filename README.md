# Roast My Profile

This project roasts GitHub profiles using Gemini AI. It consists of a FastAPI backend and a Next.js frontend.

## Prerequisites

- Python 3.8+
- Node.js 18+

## Quick Start

### 1. Backend (FastAPI)

Navigate to the `backend` directory:

```bash
cd backend
```

**Setup:**

1.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate  # macOS/Linux
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ensure you have a `.env` file in `backend/` with your `GEMINI_API_KEY`.

**Run:**

```bash
python -m uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### 2. Frontend (Next.js)

Navigate to the `frontend` directory:

```bash
cd frontend
```

**Setup:**

1.  Install dependencies:
    ```bash
    npm install
    ```

**Run:**

```bash
npm run dev
```

The frontend will run at `http://localhost:3000`.

## Features

- **Backend:** Fetches GitHub data using `requests` and generates roasts using google's `gemini-2.5-flash` model via the OpenAI client compatibility layer.
- **Frontend:** A Next.js application to display the roast.
