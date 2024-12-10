from pydantic import BaseModel
from typing import Dict, Optional

from app.models.properties.checkbox import CheckboxModel
from app.models.properties.number import NumberModel
from app.models.properties.rich_text import TitlePostModel

class MainInfoModel(BaseModel):
    title: TitlePostModel
    checkbox: CheckboxModel
    price: NumberModel

class MainInfo(BaseModel):
    properties: Dict[str, MainInfoModel]