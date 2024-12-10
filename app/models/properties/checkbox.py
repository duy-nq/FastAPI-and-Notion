from pydantic import BaseModel, Field

class Checkbox(BaseModel):
    type: str = Field(..., default='checkbox')
    checkbox: bool = Field(..., default=True)
