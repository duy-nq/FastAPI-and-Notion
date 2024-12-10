from pydantic import BaseModel, Field
from typing import Optional, List

class Text(BaseModel):
    content: Optional[str] = Field(default='Empty')

class TextProperty(BaseModel):
    text: Text

class Title(BaseModel):
    type: str = Field(default='title')
    title: List[TextProperty]

class TitleProperty(BaseModel):
    field_name: Title = Field(..., alias='Tên sản phẩm')

    class Config:
        populate_by_name = True

class Properties(BaseModel):
    properties: TitleProperty


