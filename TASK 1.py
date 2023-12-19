import os
import json

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return {"pending": [], "completed": []}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    print("Pending Tasks:")
    for i, task in enumerate(tasks["pending"], start=1):
        print(f"{i}. {task}")

    print("\nCompleted Tasks:")
    for i, task in enumerate(tasks["completed"], start=1):
        print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks["pending"].append(new_task)
    print(f"Task '{new_task}' added to the list.")

def complete_task(tasks, task_num):
    if 1 <= task_num <= len(tasks["pending"]):
        completed_task = tasks["pending"].pop(task_num - 1)
        tasks["completed"].append(completed_task)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List App ---")
        show_tasks(tasks)

        print("\n1. Add task")
        print("2. Complete task")
        print("3. Exit")

        option = input("Select an option (1/2/3): ")

        if option == "1":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif option == "2":
            task_num = int(input("Enter the task number to complete: "))
            complete_task(tasks, task_num)
        elif option == "3":
            save_tasks(tasks)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
