import tkinter as tk
from tkinter import messagebox
from todo_logic import *

tasks = load_tasks()

def refresh_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "❌"
        listbox.insert(tk.END, f"{t['task']} [{status}]")

def add():
    task = entry.get()
    if task:
        add_task(tasks, task)
        save_tasks(tasks)
        refresh_list()
        entry.delete(0, tk.END)

def delete():
    try:
        index = listbox.curselection()[0]
        delete_task(tasks, index)
        save_tasks(tasks)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

def complete():
    try:
        index = listbox.curselection()[0]
        mark_done(tasks, index)
        save_tasks(tasks)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

root = tk.Tk()
root.title("To Do List App")

entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Add Task", command=add).pack()
tk.Button(root, text="Delete Task", command=delete).pack()
tk.Button(root, text="Mark Done", command=complete).pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

refresh_list()

root.mainloop()