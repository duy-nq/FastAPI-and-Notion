from app.core.interfaces.notion_interface import NotionAPIInterface
from requests import get, patch, post
from os import getenv

class NotionClient(NotionAPIInterface):
    def __init__(self, api_token: str, database_key: str):
        self.api_token = getenv(api_token)
        self.database_id = getenv(database_key)
        self.base_url = "https://api.notion.com/v1"

    def create_subpage(self, page_data: dict):
        res = post(f'{self.base_url}/pages',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            json=page_data.model_dump(by_alias=True))
        
        return res.json()

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

    def update_main_info(self, page_id: str, main_info):              
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            json=main_info.model_dump(by_alias=True)
            )
        
        return res.json()

    def update_scientific_info(self, page_id: str, scientific_info: dict):
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            json=scientific_info.model_dump(by_alias=True)
        )
        
        return res.json()

    def update_detailed_info(self, page_id: str, detailed_info: dict):        
        res = patch(f'{self.base_url}/pages/{page_id}',
            headers={
                'Notion-Version': '2022-06-28',
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            json=detailed_info.model_dump(by_alias=True)
        )
        
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
