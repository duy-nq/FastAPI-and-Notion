from pydantic import BaseModel, Field
from os import getenv

from app.models.properties.checkbox import Checkbox
from app.models.properties.number import Number
from app.models.properties.rich_text import RichTextProperty
from app.models.properties.title import Title

class Database(BaseModel):
    database_id: str = Field(default_factory=lambda: getenv('NOTION_TREE') or "default_database_id")

class Page(BaseModel):
    title: Title = Field(..., alias='Tên sản phẩm')
    price: Number = Field(..., alias='Giá (VND)')
    in_stock: Checkbox = Field(..., alias='Còn hàng')
    scientific_name: RichTextProperty = Field(..., alias='Tên khoa học')
    attribute: RichTextProperty = Field(..., alias='Đặc điểm')
    feng_shui: RichTextProperty = Field(..., alias='Phong thủy')

    class Config:
        populate_by_name = True

class PageProperty(BaseModel):
    parent: Database
    properties: Page