from pydantic import BaseModel

class Properties(BaseModel):
    title: str
    number: int