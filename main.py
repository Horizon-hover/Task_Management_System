# main.py
from task import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            try:
                manager.add_task(title, description)
            except ValueError as e:
                print(e)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            title = input("Enter task title to mark as completed: ")
            manager.mark_task_completed(title)

        elif choice == "4":
            title = input("Enter task title to delete: ")
            manager.delete_task(title)

        elif choice == "5":
            filename = input("Enter filename to save tasks: ")
            manager.save_tasks(filename)

        elif choice == "6":
            filename = input("Enter filename to load tasks: ")
            manager.load_tasks(filename)

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()