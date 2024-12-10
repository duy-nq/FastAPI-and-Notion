from typing import List
from pydantic import BaseModel, Field

from app.models.properties.rich_text import RichTextProperty

class FengShui(BaseModel):
    property: RichTextProperty = Field(..., alias='Phong thủy')

    class Config:
        populate_by_name = True