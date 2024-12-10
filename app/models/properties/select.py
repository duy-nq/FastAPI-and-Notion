from typing import List
from pydantic import BaseModel, Field

from app.models.properties.tag import Tag

class Select(BaseModel):
    type: str = Field(default='select')
    select: Tag
