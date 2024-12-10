from pydantic import BaseModel, Field

from app.models.properties.checkbox import Checkbox

class InStock(BaseModel):
    property: Checkbox = Field(..., alias='Còn hàng')

    class Config:
        populate_by_name = True