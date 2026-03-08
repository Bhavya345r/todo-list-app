import json

def add_task(task_list, task):
    task_list.append({"task": task, "done": False})
    return task_list

def delete_task(task_list, index):
    if index < len(task_list):
        task_list.pop(index)
    return task_list

def mark_done(task_list, index):
    task_list[index]["done"] = True
    return task_list

def save_tasks(task_list, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(task_list, f)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return []