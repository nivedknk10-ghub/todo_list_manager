from task import Task

FILE_NAME = "data.txt"

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task.title} | {task.completed}\n")

def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                title, completed = line.strip().split("|")
                completed = completed.strip()
                task = Task(title)
                task.completed = completed == "True"
                tasks.append(task)
    except FileNotFoundError:
        pass

    return tasks