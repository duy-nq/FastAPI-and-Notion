from typing import List
from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect

class Humidity(BaseModel):
    property: MultiSelect = Field(..., alias='Độ ẩm')

    class Config:
        populate_by_name = True