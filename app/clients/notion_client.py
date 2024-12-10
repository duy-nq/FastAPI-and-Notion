from app.core.interfaces.notion_interface import NotionAPIInterface
from requests import get, patch
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

    def update_main_info(self, page_id: str, main_info: dict):
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            data={
                'properties': main_info
            })
        
        return res.json()

    def update_scientific_info(self, page_id: str, scientific_info: dict):
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            data={
                'properties': scientific_info
            })
        
        return res.json()

    def update_detailed_info(self, page_id: str, detailed_info: dict):
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            data={
                'properties': detailed_info
            })
        
        return res.json()

    def delete_subpage(self, page_id: str):
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            json={
                'archived': True
            })
        
        return res.json()
    
    def restore_subpage(self, page_id: str):
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            json={
                'archived': False
            })
        
        return res.json()
