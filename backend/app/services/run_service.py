from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.run_repo import RunRepository
from app.core.celery_app import celery_app

class RunService:
    def __init__(self, session: AsyncSession):
        self.repo = RunRepository(session)

    async def queue_run(self, workflow_id: int, input_payload: dict):
        run = await self.repo.create(workflow_id, input_payload)
        celery_app.send_task("workers.tasks.execute_workflow", args=[run.id])
        return run
