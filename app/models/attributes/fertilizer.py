from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Fertilizer(BaseModel):
    property: MultiSelect = Field(..., alias='Phân bón')

    class Config:
        populate_by_name = True