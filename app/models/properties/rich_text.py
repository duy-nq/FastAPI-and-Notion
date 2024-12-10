from typing import List
from pydantic import BaseModel, Field

class Text(BaseModel):
    content: str = Field(..., default='Empty')

class RichText(BaseModel):
    type: str = Field(..., default='text')
    text: Text

class RichTextProperty(BaseModel):
    type: str = Field(..., default='rich_text')
    rich_text: List[RichText]
