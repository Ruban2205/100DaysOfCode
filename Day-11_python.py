# Create a simple to-do list program.
print("Ruban Gino Singh - Day11 of #100DaysOfCode\n")

print("\nPython program to Create a ToDo List program\n")

tasks = []

def display_menu(): 
    print("\nTodo list Menu: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Clear Completed Task")
    print("5. Exit\n")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")

def mark_task_completed():
    view_tasks()
    task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def clear_completed_tasks():
    global tasks
    tasks = [task for task in tasks if not task["completed"]]
    print("Completed tasks removed!")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        clear_completed_tasks()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")