#!/usr/bin/env bash
set -e

FRONTEND_DIR="${1:-ai-automation-frontend}"
BACKEND_DIR="backend"

echo "==> Patching frontend in '$FRONTEND_DIR' and creating backend in '$BACKEND_DIR'"

# ---- Frontend ----
if [ ! -d "$FRONTEND_DIR" ]; then
  echo "ERROR: $FRONTEND_DIR not found. Create Vite app first." >&2
  exit 1
fi

pushd "$FRONTEND_DIR" >/dev/null

npm pkg delete devDependencies.@vitejs/plugin-react 2>/dev/null || true
npm i -D @vitejs/plugin-react-swc @types/react@^19 @types/react-dom@^19 typescript@latest tailwindcss postcss autoprefixer tailwindcss-animate
npm i @tanstack/react-query react-router-dom zustand ky zod reactflow react-konva echarts echarts-for-react class-variance-authority clsx tailwind-merge lucide-react sonner @tanstack/react-table

npx tailwindcss init -p || true

cat > vite.config.ts <<'EOF'
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
export default defineConfig({
  plugins: [react()],
});
EOF

cat > tailwind.config.js <<'EOF'
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: { extend: {} },
  plugins: [require("tailwindcss-animate")],
};
EOF

mkdir -p src
cat > src/index.css <<'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;
EOF

[ -f .env.local ] || echo "VITE_API_BASE=http://localhost:8000/" > .env.local

popd >/dev/null

# ---- Backend ----
mkdir -p "$BACKEND_DIR"
if command -v python3 >/dev/null 2>&1; then PY=python3; else PY=python; fi
$PY -m venv "$BACKEND_DIR/.venv"

PIP="$BACKEND_DIR/.venv/bin/pip"
PYBIN="$BACKEND_DIR/.venv/bin/python"
if [ ! -x "$PIP" ]; then
  PIP="$BACKEND_DIR/.venv/Scripts/pip.exe"
  PYBIN="$BACKEND_DIR/.venv/Scripts/python.exe"
fi

"$PIP" install -U pip wheel setuptools

cat > "$BACKEND_DIR/requirements.txt" <<'EOF'
fastapi
uvicorn[standard]
pydantic
SQLAlchemy
alembic
asyncpg
httpx
python-dotenv
EOF

"$PIP" install -r "$BACKEND_DIR/requirements.txt"

cat > "$BACKEND_DIR/main.py" <<'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
@app.get("/health")
def health():
    return {"ok": True}
EOF

echo "==> Done. Start backend then frontend:"
echo "   cd $BACKEND_DIR && $(basename "$PYBIN") -m uvicorn main:app --reload"
echo "   cd $FRONTEND_DIR && npm run dev"
