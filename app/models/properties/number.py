from pydantic import BaseModel, Field

class Number(BaseModel):
    type: str = Field(..., default='number')
    number: int