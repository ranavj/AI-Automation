from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.workflow import Workflow

class WorkflowRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, name: str, definition: dict) -> Workflow:
        wf = Workflow(name=name, definition=definition)
        self.session.add(wf)
        await self.session.commit()
        await self.session.refresh(wf)
        return wf

    async def list(self) -> list[Workflow]:
        res = await self.session.execute(select(Workflow))
        return list(res.scalars().all())
