import sqlite3
from typing import List
from .task import Task

class DatabaseHandler:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                status TEXT
            )
        ''')
        self.connection.commit()

    def save_task(self, task: Task):
        self.cursor.execute('''
            INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)
        ''', (task.title, task.description, task.status))
        self.connection.commit()

    def load_tasks(self) -> List[Task]:
        self.cursor.execute('SELECT * FROM tasks')
        records = self.cursor.fetchall()
        return [Task(*record) for record in records]
  
    def close(self):
        self.connection.close()