from app.clients.notion_client import NotionClient

def get_notion_client():
    return NotionClient(api_token="NOTION_KEY", database_key="NOTION_TREE")