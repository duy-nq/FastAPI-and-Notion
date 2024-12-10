from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Method(BaseModel):
    property: MultiSelect = Field(..., alias='Nhân giống')

    class Config:
        populate_by_name = True