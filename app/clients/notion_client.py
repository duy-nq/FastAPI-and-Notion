from app.core.interfaces.notion_interface import NotionAPIInterface

class NotionClient(NotionAPIInterface):
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.notion.com/v1/"

    def create_subpage(self, page_data: dict):
        # Implementation for creating a subpage
        pass

    def read_subpage(self, page_id: str):
        # Implementation for reading a subpage
        pass

    def update_subpage(self, page_id: str, page_data: dict):
        # Implementation for updating a subpage
        pass

    def delete_subpage(self, page_id: str):
        # Implementation for deleting a subpage
        pass
