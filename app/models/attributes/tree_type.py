from typing import List
from pydantic import BaseModel, Field

from app.models.properties.select import Select

class TreeType(BaseModel):
    property: Select = Field(..., alias='Nhóm cây')

    class Config:
        populate_by_name = True