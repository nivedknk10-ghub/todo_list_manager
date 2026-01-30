#this it the main file
from manager import Taskmanager

def main():
    manager = Taskmanager()

    manager.add_task("Learn OSINT")
    manager.add_task("Buy Galaxy A36 5G")

    manager.list_tasks()
    manager.complete_task(1)
    print("\nAfter completing the first task:\n")
    manager.list_tasks()

if __name__ == "__main__":
    main()
