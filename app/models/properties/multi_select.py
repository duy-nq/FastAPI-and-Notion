from typing import List, Optional
from pydantic import BaseModel

# POST Models
class MultiSelectPostBaseModel(BaseModel):
    name: str
    color: Optional[str]  # Optional to allow user to specify color if supported

class MultiSelectPostPayloadModel(BaseModel):
    multi_select_post: List[MultiSelectPostBaseModel]

# GET Models
class MultiSelectGetBaseModel(BaseModel):
    id: str
    name: str
    color: str

class MultiSelectGetModel(BaseModel):
    id: str
    name: str
    type: str
    multi_select: List[MultiSelectGetBaseModel]

class MultiSelectGetPayloadModel(BaseModel):
    multi_select_get: MultiSelectGetModel
