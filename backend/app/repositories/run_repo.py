from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.run import Run

class RunRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, workflow_id: int, input_payload: dict) -> Run:
        run = Run(workflow_id=workflow_id, input_payload=input_payload, status="queued")
        self.session.add(run)
        await self.session.commit()
        await self.session.refresh(run)
        return run

    async def get(self, run_id: int) -> Run | None:
        res = await self.session.execute(select(Run).where(Run.id == run_id))
        return res.scalar_one_or_none()
