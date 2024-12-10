from pydantic import BaseModel, Field

class MainInfo(BaseModel):
    title: str = Field(default=None)
    checkbox: bool = Field(default=None)
    price: int = Field(default=None)