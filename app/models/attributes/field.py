from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Field(BaseModel):
    property: MultiSelect = Field(..., alias='Đất')

    class Config:
        populate_by_name = True