from typing import List
from src.task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}  

    def create_task(self, title: str, description: str) -> Task:
        if not title:
            raise ValueError("Название задачи не может быть пустым")
        
        id = len(self.tasks) + 1
        new_task = Task(id, title, description, "не выполнено")
        self.tasks[id] = new_task
        return new_task

    def read_tasks(self) -> List[Task]:
        return list(self.tasks.values())
    
    def update_task(self, id: int, status: str):
        if id not in self.tasks:
            raise ValueError("Задача не найдена")
        self.tasks[id].status = status
    
    def delete_task(self, id: int):
        if id not in self.tasks:
            raise ValueError("Задача не найдена")
        del self.tasks[id]