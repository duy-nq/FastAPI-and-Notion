from typing import Optional
from pydantic import BaseModel

class CheckboxPostModel(BaseModel):
    checkbox: bool

class CheckboxGetModel(BaseModel):
    id: Optional[str]
    type: Optional[str]
    checkbox: bool

class CheckboxPayloadModel(BaseModel):
    Task_completed: Optional[CheckboxGetModel] = None
    properties: Optional[dict] = None
