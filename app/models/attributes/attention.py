from typing import List
from pydantic import BaseModel, Field

from app.models.properties.rich_text import RichTextProperty

class Attention(BaseModel):
    property: RichTextProperty = Field(..., alias='Lưu ý')

    class Config:
        populate_by_name = True