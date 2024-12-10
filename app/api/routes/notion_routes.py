from fastapi import APIRouter, Depends
from app.models.notion.main_info import MainInfoProperty
from app.models.notion.scientific_info import ScientificInfoProperty
from app.models.properties.title import Properties
from app.services.notion_service import NotionService
from app.core.dependencies import get_notion_client
from app.clients.notion_client import NotionClient

router = APIRouter()

# @router.post("/page", response_model=None)
# def create_page(page: Page, client: NotionClient = Depends(get_notion_client)):
#     service = NotionService(client)
#     return service.create_page(page)

@router.get("/page-view")
def read_page(page_id: str, client: NotionClient = Depends(get_notion_client)):
    service = NotionService(client)
    return service.get_page(page_id=page_id)

@router.patch("/page-update")
def update_page():
    pass

@router.patch("/page-update-main")
def update_main_info(page_id: str,
                     newdata: MainInfoProperty,
                     client: NotionClient = Depends(get_notion_client)): 
    
    service = NotionService(client)
    return service.update_main_info(page_id=page_id, data=newdata)

@router.patch("/page-update-scientific")
def update_scientific_info(page_id: str,
                     newdata: ScientificInfoProperty,
                     client: NotionClient = Depends(get_notion_client)):
    
    service = NotionService(client)
    return service.update_scientific_info(page_id=page_id, data=newdata)

@router.patch("/page-update-detail")
def update_detailed_info():
    pass

@router.patch("/page-delete")
def delete_page(page_id: str, client: NotionClient = Depends(get_notion_client)):
    service = NotionService(client)
    return service.delete_page(page_id=page_id)

@router.patch("/page-restore")
def delete_page(page_id: str, client: NotionClient = Depends(get_notion_client)):
    service = NotionService(client)
    return service.restore_page(page_id=page_id)