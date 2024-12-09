from fastapi import APIRouter, Depends
from app.services.notion_service import NotionService
from app.core.dependencies import get_notion_client
from app.models.notion_page import Page
from app.clients.notion_client import NotionClient

router = APIRouter()

@router.post("/pages")
def create_page(page: Page, client: NotionClient = Depends(get_notion_client)):
    service = NotionService(client)
    return service.create_page(page)