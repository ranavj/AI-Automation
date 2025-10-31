from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.workflow_repo import WorkflowRepository

class WorkflowService:
    def __init__(self, session: AsyncSession):
        self.repo = WorkflowRepository(session)

    async def create_workflow(self, name: str, definition: dict):
        return await self.repo.create(name, definition)

    async def list_workflows(self):
        return await self.repo.list()
