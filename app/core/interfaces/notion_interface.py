from abc import ABC, abstractmethod

class NotionAPIInterface(ABC):
    @abstractmethod
    def create_subpage(self, page_data: dict):
        """Create a new subpage in the Notion database."""
        pass

    @abstractmethod
    def read_subpage(self, page_id: str):
        """Retrieve details of a specific subpage."""
        pass

    @abstractmethod
    def update_subpage(self, page_id: str, page_data: dict):
        """Update the details of a specific subpage."""
        pass

    @abstractmethod
    def delete_subpage(self, page_id: str):
        """Delete a subpage from the Notion database."""
        pass
