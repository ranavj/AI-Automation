from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.schemas.workflow import WorkflowCreate, WorkflowOut
from app.services.workflow_service import WorkflowService

router = APIRouter(prefix="/workflows", tags=["workflows"])

@router.post("/", response_model=WorkflowOut)
async def create_workflow(payload: WorkflowCreate, session: AsyncSession = Depends(get_session)):
    svc = WorkflowService(session)
    wf = await svc.create_workflow(payload.name, payload.definition)
    return wf

@router.get("/", response_model=list[WorkflowOut])
async def list_workflows(session: AsyncSession = Depends(get_session)):
    svc = WorkflowService(session)
    return await svc.list_workflows()
