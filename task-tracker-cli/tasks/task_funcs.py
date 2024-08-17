import json
import os
from contextlib import contextmanager
from datetime import datetime

TASKS_FILE = 'tasks.json'


@contextmanager
def tasks_file_manager(mode='r'):
    try:
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'w') as f:
                f.write('[]')

        with open(TASKS_FILE, mode) as f:
            if mode == 'r':
                try:
                    yield json.load(f)
                except json.JSONDecodeError:
                    yield []
            else:
                yield f
    except IOError:
        print('Error: Please check file permissions.')
        yield None


def get_tasks():
    with tasks_file_manager() as tasks:
        return tasks if tasks is not None else "No tasks found."


def save_tasks(tasks):
    with tasks_file_manager('w') as f:
        json.dump(tasks, f, indent=2)
        print('Tasks saved successfully.')


def add_task(description, status="todo"):
    tasks = get_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": status,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return f"Task added successfully with id: {new_task['id']}"


def update_task(task_id, description):
    tasks = get_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updated_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            return f"Task {task_id} updated successfully."
    return f"Task {task_id} not found."


def delete_task(task_id):
    tasks = get_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return f"Task {task_id} deleted successfully."
    return f"Task {task_id} not found."


def update_task_status(task_id, status):
    print(task_id, status)
    tasks = get_tasks()
    print(tasks)
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updated_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            return f"Task {task_id} status updated to {status}"
    return f"Task {task_id} not found."


def list_tasks(status=None):
    tasks = get_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    return tasks
