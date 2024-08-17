import argparse as ar

from tasks import task_funcs


def main():
    parser = ar.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument(
        "--status", choices=["todo", "in-progress", "done"], default="todo", help="Task status")

    # Update task
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", help="New task description")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # update task status
    mark_parser = subparsers.add_parser("mark", help="Mark task status")
    mark_parser.add_argument("id", type=int, help="Task ID")
    mark_parser.add_argument(
        "status", choices=["todo", "in-progress", "done"], help="Task status")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status", choices=["todo", "in-progress", "done"], help="Filter by status")

    args = parser.parse_args()

    if args.command == "add":
        print(task_funcs.add_task(args.description, args.status))
    elif args.command == "update":
        print(task_funcs.update_task(args.id, args.description))
    elif args.command == "delete":
        print(task_funcs.delete_task(args.id))
    elif args.command == "mark":
        print(task_funcs.update_task_status(args.id, args.status))
    elif args.command == "list":
        task_list = task_funcs.list_tasks(args.status)
        for task in task_list:
            print(
                f"ID: {task['id']}, Status: {task['status']}, Description: {task['description']}")


if __name__ == "__main__":
    main()
