# Simple To-Do List Manager

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Manager")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks in your list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "Complete" if task['complete'] else "Incomplete"
            print(f"{idx}. {task['task']} - {status}")

# Function to add a new task
def add_task():
    task_name = input("\nEnter the new task: ")
    tasks.append({"task": task_name, "complete": False})
    print(f"Task '{task_name}' added.")

# Function to mark a task as complete
def complete_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['complete'] = True
        print(f"Task '{tasks[task_number]['task']}' marked as complete.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-5): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid option. Please try again.")
