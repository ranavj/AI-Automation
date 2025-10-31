from app.core.celery_app import celery_app

@celery_app.task(name="workers.tasks.execute_workflow")
def execute_workflow(run_id: int) -> dict:
    # TODO: DB fetch/update if needed
    return {"run_id": run_id, "status": "success"}
