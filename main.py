#this it the main file
from task import Task

def main():
    task1 = Task("Learn github workflow")
    print(task1.title)
    print(task1.completed)

    task1.mark_completed()
    print(task1.completed)

if __name__ == "__main__":
    main()
