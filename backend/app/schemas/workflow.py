from pydantic import BaseModel, Field, ConfigDict
from typing import Any, Dict

class WorkflowCreate(BaseModel):
    name: str
    definition: Dict[str, Any] = Field(default_factory=dict)

class WorkflowOut(BaseModel):
    id: int
    name: str
    definition: Dict[str, Any]
    # v2 style config
    model_config = ConfigDict(from_attributes=True)
