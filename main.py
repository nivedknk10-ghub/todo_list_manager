from manager import Taskmanager

def show_menu():
    print("\nTo-Do List Manager\n")
    print("1. Add Task\n")
    print("2. View Task\n")
    print("3. Complete Task\n")
    print("4. Exit\n")

def main():
    manager = Taskmanager()

    while True:
        show_menu()
        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            title = input("Enter Task Title: ")
            manager.add_task(title)
            print("Task Added")

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            number = int(input("Enter Task Number: "))
            manager.complete_task(number)
            print("Task Completed")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
