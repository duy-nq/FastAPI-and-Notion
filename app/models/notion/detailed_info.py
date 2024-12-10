from pydantic import BaseModel, Field

from app.models.properties.multi_select import MultiSelect
from app.models.properties.rich_text import RichTextProperty
from app.models.properties.select import Select

class DetailedInfo(BaseModel):
    tree_type: Select = Field(..., alias='Nhóm cây')
    light: MultiSelect = Field(..., alias='Ánh sáng')
    field: MultiSelect = Field(..., alias='Đất')
    water: MultiSelect = Field(..., alias='Tưới nước')
    humidity: MultiSelect = Field(..., alias='Độ ẩm')
    temperature: MultiSelect = Field(..., alias='Nhiệt độ')
    fertilizer: MultiSelect = Field(..., alias='Phân bón')
    method: MultiSelect = Field(..., alias='Nhân giống')
    attention: RichTextProperty = Field(..., alias='Lưu ý')

    class Config:
        populate_by_name = True

class DetailedInfoProperty(BaseModel):
    properties: DetailedInfo