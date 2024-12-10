from fastapi import APIRouter, Depends
from app.services.notion_service import NotionService
from app.core.dependencies import get_notion_client
from app.models.notion_page import Page
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

@router.get("/database-view")
def read_database(database_id: str, client: NotionClient = Depends(get_notion_client)):
    service = NotionService(client)
    return service.get_database(database_id=database_id)

@router.patch("/page-update")
def update_page():
    pass

@router.patch("/page-delete")
def delete_page():
    pass