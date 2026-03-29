import json

tasks = []

def show_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i + 1}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added.")

def mark_complete():
    view_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks()
        print("Task marked as complete.")
    except:
        print("Invalid input.")

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

while True:
    load_tasks()
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
