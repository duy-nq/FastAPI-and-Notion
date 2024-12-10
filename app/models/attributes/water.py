from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Water(BaseModel):
    property: MultiSelect = Field(..., alias='Tưới nước')

    class Config:
        populate_by_name = True