class Page:
    def __init__(self, title: str, content: str = "", page_id: str = None):
        self.title = title
        self.content = content
        self.page_id = page_id

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content
        }