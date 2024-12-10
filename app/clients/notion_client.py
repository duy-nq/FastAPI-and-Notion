from app.core.interfaces.notion_interface import NotionAPIInterface
from requests import get
from os import getenv

class NotionClient(NotionAPIInterface):
    def __init__(self, api_token: str, database_key: str):
        self.api_token = getenv(api_token)
        self.database_id = getenv(database_key)
        self.base_url = "https://api.notion.com/v1"

    def create_subpage(self, page_data: dict):
        # Implementation for creating a subpage
        pass

    def read_subpage(self, page_id: str):
        res = get(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}'
            })
        
        return res.json()
        
    def update_subpage(self, page_id: str, page_data: dict):
        # Implementation for updating a subpage
        pass

    def delete_subpage(self, page_id: str):
        # Implementation for deleting a subpage
        pass
