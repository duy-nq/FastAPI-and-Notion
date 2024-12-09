from app.clients.notion_client import NotionClient

def get_notion_client():
    return NotionClient(api_token="your_notion_api_token")