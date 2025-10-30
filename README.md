AI + Automation

React 19 (Vite + TS) frontend + FastAPI backend for building simple “Gmail → Slack → Jira” style automations.

Tech Stack

Frontend: React 19, TypeScript, Vite, React Router, React Query, Zustand, Tailwind (+ shadcn/ui), React Flow

Backend: FastAPI, Uvicorn, Pydantic

(DB later: PostgreSQL suggested)

Structure
AI+Automation/
├─ ai-automation-frontend/   # React app
└─ backend/                  # FastAPI app
   ├─ main.py
   └─ requirements.txt

Setup
Backend
cd backend
# create & activate venv
python -m venv .venv
# Windows
.venv\Scripts\python.exe -m pip install -U pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000
# macOS/Linux (activate then use `python -m pip ...`)

Frontend
cd ai-automation-frontend
npm install
# configure API base if needed:
# echo VITE_API_BASE=http://localhost:8000/ > .env.local
npm run dev


Open:

API: http://localhost:8000/health
 → { "ok": true }

Web: Vite dev URL (e.g., http://localhost:5173
)

Notes

Don’t commit: .venv/, node_modules/, dist/, .env*

Update backend deps by editing backend/requirements.txt (then reinstall).
