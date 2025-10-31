
# Quickstart

# 1) Copy .env
cp .env.example .env
# If using Docker:
make up
# FastAPI available at http://localhost:8000/docs

# OR local (no Docker):
python -m venv .venv && source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload