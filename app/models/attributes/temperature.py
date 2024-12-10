from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Temperature(BaseModel):
    property: MultiSelect = Field(..., alias='Nhiệt độ')

    class Config:
        populate_by_name = True