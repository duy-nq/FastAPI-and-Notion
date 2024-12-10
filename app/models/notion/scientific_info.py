from pydantic import BaseModel, Field

from app.models.properties.rich_text import RichTextProperty

class ScientificInfo(BaseModel):
    scientific_name: RichTextProperty = Field(..., alias='Tên khoa học')
    attribute: RichTextProperty = Field(..., alias='Đặc điểm')
    feng_shui: RichTextProperty = Field(..., alias='Phong thủy')

    class Config:
        populate_by_name = True

class ScientificInfoProperty(BaseModel):
    properties: ScientificInfo