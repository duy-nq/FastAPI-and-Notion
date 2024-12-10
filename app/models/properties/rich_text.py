from typing import List, Optional
from pydantic import BaseModel

# Shared models for rich text components
class TextModel(BaseModel):
    content: str
    link: Optional[str]

class AnnotationsModel(BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str

class RichTextModel(BaseModel):
    type: str
    text: TextModel
    annotations: AnnotationsModel
    plain_text: str
    href: Optional[str]

# Model for POST payload
class RichTextPostModel(BaseModel):
    rich_text: List[RichTextModel]

class RichTextPostModel(BaseModel):
    Description: RichTextPostModel

class RichTextPostPayloadModel(BaseModel):
    properties: RichTextPostModel

# Model for GET payload
class RichTextGetModel(BaseModel):
    id: str
    type: str
    rich_text: List[RichTextModel]

class RichTextGetPayloadModel(BaseModel):
    Description: RichTextGetModel
