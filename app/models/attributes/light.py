from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Light(BaseModel):
    property: MultiSelect = Field(..., alias='Ánh sáng')

    class Config:
        populate_by_name = True