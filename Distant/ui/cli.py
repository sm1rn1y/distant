import sys
from src.task_manager import TaskManager
from src.database_handler import DatabaseHandler

def main():
    task_manager = TaskManager()
    db_handler = DatabaseHandler('database/task_manager.db')

    try:
        # Загрузка существующих задач
        tasks = db_handler.load_tasks()
        for task in tasks:
            task_manager.tasks[task.id] = task
        
        while True:
            print("\n1. Добавить задачу\n2. Показать все задачи\n3. Изменить статус\n4. Удалить задачу\n5. Выход")
            choice = input("Выберите действие: ")
            
            if choice == '1':
                title = input("Введите название задачи: ")
                description = input("Введите описание задачи: ")
                task_manager.create_task(title, description)
            elif choice == '2':
                for task in task_manager.read_tasks():
                    print(task)
            elif choice == '3':
                id = int(input("Введите id задачи для изменения статуса: "))
                status = input("Введите новый статус: ")
                task_manager.update_task(id, status)
            elif choice == '4':
                id = int(input("Введите id задачи для удаления: "))
                task_manager.delete_task(id)
            elif choice == '5':
                break
            else:
                print("Неправильный ввод. Пожалуйста, попробуйте еще раз.")
    finally:
        db_handler.close()

if __name__ == "__main__":
    main()