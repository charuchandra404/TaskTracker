import argparse
import json
import os


TASKS_FILE = "TASKS.json"
def initialize_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)

def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "not done"})
    save_tasks(tasks)
    print(f"Task added: {description} (ID: {task_id})")

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    #add logic to print task

def delete_task(taskid):
    tasks = load_tasks()
    updated_tasks = [tasks for tasks in tasks if tasks["id"] != taskid]
    save_tasks(updated_tasks)
    print(f"Deleting {taskid}")

def update_task(taskid, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == taskid:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task updated: {new_description} (ID: {taskid})")
            return
    print(f"Task with ID {taskid} not found.")

def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print(f"Task status updated to '{status}' (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI - A simple tool to manage your tasks.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="The task description")

    list_parser = subparsers.add_parser("list", help="List all tasks")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("taskid",  type=int, help="The task to delete")

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, help="The ID of the task to update")
    update_parser.add_argument("new_description", type=str, help="The new task description")


    status_parser = subparsers.add_parser("status", help="Change the status of a task")
    status_parser.add_argument("task_id", type=int, help="The ID of the task")
    status_parser.add_argument("status", type=str, choices=["not done", "in progress", "done"], help="The new status")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.task_id, args.new_description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "status":
        change_status(args.task_id, args.status)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
