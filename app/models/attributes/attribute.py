from typing import List
from pydantic import BaseModel, Field

from app.models.properties.rich_text import RichTextProperty

class Attribute(BaseModel):
    property: RichTextProperty = Field(..., alias='Đặc điểm')

    class Config:
        populate_by_name = True