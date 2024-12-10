from typing import List
from pydantic import BaseModel, Field

from app.models.properties.tag import Tag

class MultiSelect(BaseModel):
    type: str = Field(default='multi_select')
    multi_select: List[Tag]
