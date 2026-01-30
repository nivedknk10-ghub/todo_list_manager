from task import Task
from storage import save_tasks, load_tasks

class Taskmanager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        save_tasks(self.tasks)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return

        for index, task in enumerate(self.tasks):
            status = "Done" if task.completed else "Pending"
            print(f"{index +1}.{task.title}: {[status]}")

    def complete_task(self, task_number):
        if 1<=task_number<=len(self.tasks):
            task = self.tasks[task_number-1].mark_completed()
            save_tasks(self.tasks)
        else:
            print("Invalid task number")