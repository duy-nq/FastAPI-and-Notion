from pydantic import BaseModel, Field

from app.models.properties.checkbox import Checkbox
from app.models.properties.number import Number
from app.models.properties.title import Title

class MainInfo(BaseModel):
    title: Title = Field(..., alias='Tên sản phẩm')
    price: Number = Field(..., alias='Giá (VND)')
    in_stock: Checkbox = Field(..., alias='Còn hàng')

    class Config:
        populate_by_name = True

class MainInfoProperty(BaseModel):
    properties: MainInfo