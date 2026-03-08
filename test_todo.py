from todo_logic import add_task, delete_task, mark_done

def test_add_task():
    tasks = []
    tasks = add_task(tasks, "Study Python")
    assert tasks[0]["task"] == "Study Python"

def test_delete_task():
    tasks = [{"task": "Test", "done": False}]
    tasks = delete_task(tasks, 0)
    assert tasks == []

def test_mark_done():
    tasks = [{"task": "Test", "done": False}]
    tasks = mark_done(tasks, 0)
    assert tasks[0]["done"] == True