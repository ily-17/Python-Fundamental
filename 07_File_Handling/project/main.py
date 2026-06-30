import json
import os

FILE_NAME = "tasks.json"


# -----------------------------
# Load Tasks
# -----------------------------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# -----------------------------
# Save Tasks
# -----------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Add Task
# -----------------------------
def add_task(tasks):
    task = input("Enter task: ")

    tasks.append({
        "task": task,
        "done": False
    })

    save_tasks(tasks)

    print("✅ Task Added Successfully")


# -----------------------------
# View Tasks
# -----------------------------
def view_tasks(tasks):

    if not tasks:
        print("\nNo Tasks Found\n")
        return

    print("\n------ TASKS ------")

    for i, task in enumerate(tasks, start=1):

        status = "✅" if task["done"] else "❌"

        print(f"{i}. {task['task']} {status}")

    print()


# -----------------------------
# Mark Complete
# -----------------------------
def mark_complete(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number: "))

        tasks[number - 1]["done"] = True

        save_tasks(tasks)

        print("Task Completed")

    except (ValueError, IndexError):
        print("Invalid Task Number")


# -----------------------------
# Delete Task
# -----------------------------
def delete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number: "))

        removed = tasks.pop(number - 1)

        save_tasks(tasks)

        print(f"{removed['task']} Deleted")

    except (ValueError, IndexError):
        print("Invalid Task Number")


# -----------------------------
# Main Program
# -----------------------------
def main():

    tasks = load_tasks()

    while True:

        print("\n========== TODO APP ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_task(tasks)

            elif choice == 2:
                view_tasks(tasks)

            elif choice == 3:
                mark_complete(tasks)

            elif choice == 4:
                delete_task(tasks)

            elif choice == 5:
                print("Goodbye!")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
