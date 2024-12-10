from pydantic import BaseModel, Field

from app.models.properties.number import Number

class Price(BaseModel):
    property: Number = Field(..., alias='Giá (VND)')

    class Config:
        populate_by_name = True