import argparse

def add_task(task):
    print(f"Adding {task}")

def list_tasks():
    print("Listing all tasks")
    #add logic to print task

def delet_task(taskId):
    print(f"Deleting {taskId}")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI - A simple tool to manage your tasks.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task to add")

    list_parser = subparsers.add_parser("list", help="List all tasks")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("taskId",  type=int, help="The task to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        delet_task(args.taskId)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
