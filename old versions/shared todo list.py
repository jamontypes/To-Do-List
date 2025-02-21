import tkinter as tk
from tkinter import messagebox


def add_task():
    # Function to add a new task
    pass


def edit_task(task_id):
    # Function to edit an existing task
    pass


def delete_task(task_id):
    # Function to delete an existing task
    pass


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the header
header_frame = tk.Frame(root, bg='grey')
header_frame.pack(fill=tk.X)

# Create the "Create Task" button
create_task_button = tk.Button(header_frame, text="+ Create Task", command=add_task)
create_task_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create the "Sort by" and "Group By" options
sort_button = tk.Button(header_frame, text="Sort by Date ↓")
sort_button.pack(side=tk.LEFT, padx=5, pady=5)
group_button = tk.Button(header_frame, text="Group By Priority ↓")
group_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create the main task list area
task_list_frame = tk.Frame(root)
task_list_frame.pack(fill=tk.BOTH, expand=True)

# Example tasks (in a real application, this could be populated from a database or file)
tasks = [
    {"name": "Go to Class", "time": "8 AM Today"},
    {"name": "Walk Dog", "time": "1 PM Daily"},
    # ... add more tasks
]

# Display the tasks in the task list area
for task in tasks:
    task_frame = tk.Frame(task_list_frame)
    task_frame.pack(fill=tk.X, padx=5, pady=5)

    priority_indicator = tk.Label(task_frame, text="●", fg="orange")
    priority_indicator.pack(side=tk.LEFT)

    task_name = tk.Label(task_frame, text=task["name"])
    task_name.pack(side=tk.LEFT, fill=tk.X, expand=True)

    task_time = tk.Label(task_frame, text=task["time"])
    task_time.pack(side=tk.LEFT)

    edit_button = tk.Button(task_frame, text="✏️", command=lambda: edit_task(task["name"]))
    edit_button.pack(side=tk.LEFT)

    delete_button = tk.Button(task_frame, text="🗑️", command=lambda: delete_task(task["name"]))
    delete_button.pack(side=tk.LEFT)

# Run the application
root.mainloop()