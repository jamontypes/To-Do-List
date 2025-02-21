import csv
import os
import tkinter as tk
import datetime

class TaskManager:
    def __init__(self, master, listbox_tasks):
        self.master = master
        master.title("Task Manager")
        master.geometry("700x500")

        self.create_file()

        self.label = tk.Label(master, text="TO DO", font=("Helvetica", 16))
        self.label.pack()

        self.options_frame = tk.Frame(master)
        self.options_frame.pack(side=tk.LEFT, fill=tk.Y)  # Position options_frame on the left side

        self.new_task_button = tk.Button(self.options_frame, text="Create New Task", command=self.new_task)
        self.new_task_button.pack()

        self.delete_task_button = tk.Button(self.options_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.edit_task_button = tk.Button(self.options_frame, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack()

        self.sort = tk.Button(self.options_frame, text="Sort By", command=self.sort_by)
        self.sort.pack()

        self.group = tk.Button(self.options_frame, text="Group By", command=self.group_by)
        self.group.pack()

        self.listbox_tasks = listbox_tasks  # Store listbox_tasks as an attribute
        self.listbox_tasks.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)  # Position listbox_tasks on the right side
        self.show_tasks()

    def create_file(self):
        if not os.path.isfile("database.csv"):
            with open('database.csv', 'w', newline='') as csvfile:
                fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    def get_last_task_id(self):
        if os.path.isfile("database.csv"):
            with open('database.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                tasks = list(reader)
                if tasks:
                    last_task = tasks[-1]
                    return int(last_task['task_id'])
        return 0

    def new_task(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("New Task")

        self.name_label = tk.Label(self.new_window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.new_window)
        self.name_entry.pack()

        self.description_label = tk.Label(self.new_window, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.new_window)
        self.description_entry.pack()

        self.date_label = tk.Label(self.new_window, text="Date (MM/DD/YY):")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.new_window)
        self.date_entry.pack()

        self.time_label = tk.Label(self.new_window, text="Time (HH:MM AM/PM):")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.new_window)
        self.time_entry.pack()

        self.interval_label = tk.Label(self.new_window, text="Interval:")
        self.interval_label.pack()
        self.interval_entry = tk.Entry(self.new_window)
        self.interval_entry.pack()

        self.priority_label = tk.Label(self.new_window, text="Priority:")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(self.new_window)
        self.priority_entry.pack()

        self.submit_button = tk.Button(self.new_window, text="Submit", command=self.write2file)
        self.submit_button.pack()

        self.show_tasks()

    def write2file(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        interval = self.interval_entry.get()
        priority = self.priority_entry.get()


        last_task_id = self.get_last_task_id()
        next_task_id = last_task_id + 1

        with open('database.csv', 'a', newline='') as csvfile:
            fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval','Priority']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'task_id': next_task_id,
                'Names': name,
                'Descriptions': description,
                'Dates': date,
                'Times': time,
                'Interval': interval,
                'Priority': priority
            })

        self.new_window.destroy()

    def delete_task(self):
        selected_task_index = self.listbox_tasks.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            selected_task_info = self.listbox_tasks.get(selected_task_index)
            task_id = int(selected_task_info.split(':')[0])
            with open('database.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = [row for row in reader if int(row['task_id']) != task_id]

            with open('database.csv', 'w', newline='') as csvfile:
                fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            # Refresh task list
            self.show_tasks()

    def edit_task(self):
        selected_task_index = self.listbox_tasks.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            selected_task_info = self.listbox_tasks.get(selected_task_index)
            task_id = int(selected_task_info.split(':')[0])

            with open('database.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for task in reader:
                    if int(task['task_id']) == task_id:
                        self.new_window = tk.Toplevel(self.master)
                        self.new_window.title("Edit Task")

                        self.name_label = tk.Label(self.new_window, text="Name:")
                        self.name_label.pack()
                        self.name_entry = tk.Entry(self.new_window)
                        self.name_entry.insert(0, task['Names'])
                        self.name_entry.pack()

                        self.description_label = tk.Label(self.new_window, text="Description:")
                        self.description_label.pack()
                        self.description_entry = tk.Entry(self.new_window)
                        self.description_entry.insert(0, task['Descriptions'])
                        self.description_entry.pack()

                        self.date_label = tk.Label(self.new_window, text="Date (MM/DD/YY):")
                        self.date_label.pack()
                        self.date_entry = tk.Entry(self.new_window)
                        self.date_entry.insert(0, task['Dates'])
                        self.date_entry.pack()

                        self.time_label = tk.Label(self.new_window, text="Time (HH:MM AM/PM):")
                        self.time_label.pack()
                        self.time_entry = tk.Entry(self.new_window)
                        self.time_entry.insert(0, task['Times'])
                        self.time_entry.pack()

                        self.interval_label = tk.Label(self.new_window, text="Interval:")
                        self.interval_label.pack()
                        self.interval_entry = tk.Entry(self.new_window)
                        self.interval_entry.insert(0, task['Interval'])
                        self.interval_entry.pack()

                        self.priority_label = tk.Label(self.new_window, text="Priority:")
                        self.priority_label.pack()
                        self.priority_entry = tk.Entry(self.new_window)
                        self.priority_entry.insert(0, task['Priority'])
                        self.priority_entry.pack()

                        self.submit_button = tk.Button(self.new_window, text="Submit",command=lambda: self.update_task(task_id))
                        self.submit_button.pack()

                        break

    def update_task(self, task_id):
        name = self.name_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        interval = self.interval_entry.get()
        priority = self.priority_entry.get

        with open('database.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row if int(row['task_id']) != task_id else {
                'task_id': task_id,
                'Names': name,
                'Descriptions': description,
                'Dates': date,
                'Times': time,
                'Interval': interval,
                'Priority': priority
            } for row in reader]

        with open('database.csv', 'w', newline='') as csvfile:
            fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        self.new_window.destroy()
        self.show_tasks()


    def show_tasks(self):
        self.listbox_tasks.delete(0, tk.END)
        if os.path.isfile("database.csv"):
            with open('database.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for task in reader:
                    task_info = f"{task['task_id']}: {task['Names']} {task['Descriptions']} - Due: {task['Dates']} {task['Times']}    Priority:{task['Priority']}"
                    self.listbox_tasks.insert(tk.END, task_info)
        else:
            self.listbox_tasks.insert(tk.END, "No tasks found.")

    def sort_by(self):
        sort_window = tk.Toplevel(self.master)
        sort_window.title("Sort By")

        btn_descending = tk.Button(sort_window, text="Descending Date")
        btn_descending.pack()
        btn_ascending = tk.Button(sort_window, text="Ascending Date")
        btn_ascending.pack()

    def group_by(self):
        pass

def main():
    root = tk.Tk()
    listbox_tasks = tk.Listbox(root)
    listbox_tasks.pack()
    app = TaskManager(root, listbox_tasks)
    app.show_tasks()
    root.mainloop()

if __name__ == "__main__":
    main()
