from app.core.interfaces.notion_interface import NotionAPIInterface
from app.models.notion_page import Page

class NotionService:
    def __init__(self, notion_client: NotionAPIInterface):
        self.notion_client = notion_client

    def create_page(self, page: Page):
        return self.notion_client.create_subpage(page.to_dict())

    def get_page(self, page_id: str):
        return self.notion_client.read_subpage(page_id)

    def update_page(self, page: Page):
        return self.notion_client.update_subpage(page.page_id, page.to_dict())

    def delete_page(self, page_id: str):
        return self.notion_client.delete_subpage(page_id)
