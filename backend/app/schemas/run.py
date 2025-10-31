from pydantic import BaseModel, ConfigDict
from typing import Any, Dict

class RunCreate(BaseModel):
    workflow_id: int
    input_payload: Dict[str, Any] = {}

class RunOut(BaseModel):
    id: int
    workflow_id: int
    status: str
    output_payload: Dict[str, Any]
    model_config = ConfigDict(from_attributes=True)
