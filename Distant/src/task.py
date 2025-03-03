class Task:
    def __init__(self, id: int, title: str, description: str, status: str):
        self.id = id
        self.title = title
        self.description = description
        self.status = status  
    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, description={self.description}, status={self.status})"