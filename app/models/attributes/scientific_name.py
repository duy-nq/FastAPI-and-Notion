from typing import List
from pydantic import BaseModel, Field

from app.models.properties.rich_text import RichTextProperty

class ScientificName(BaseModel):
    property: RichTextProperty = Field(..., alias='Tên khoa học')

    class Config:
        populate_by_name = True