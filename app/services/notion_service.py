from app.core.interfaces.notion_interface import NotionAPIInterface
from app.models.notion.main_info import MainInfo
from app.models.notion.scientific_info import ScientificInfo
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
    
    def update_main_info(self, page_id: str, data: MainInfo):
        return self.notion_client.update_main_info(page_id, data)

    def update_scientific_info(self, page_id: str, data: ScientificInfo):
        self.notion_client.update_scientific_info(page_id, data)

    def update_detailed_info(self, page: Page):
        pass

    def delete_page(self, page_id: str):
        return self.notion_client.delete_subpage(page_id)

    def restore_page(self, page_id: str):
        return self.notion_client.restore_subpage(page_id)