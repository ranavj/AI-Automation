from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.schemas.run import RunCreate, RunOut
from app.services.run_service import RunService

router = APIRouter(prefix="/runs", tags=["runs"])

@router.post("/", response_model=RunOut)
async def queue_run(payload: RunCreate, session: AsyncSession = Depends(get_session)):
    svc = RunService(session)
    run = await svc.queue_run(payload.workflow_id, payload.input_payload)
    return run
