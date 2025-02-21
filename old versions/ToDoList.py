import csv
import os
import tkinter as tk
import datetime
#still no current use of date time but will use for the wake system/alarm for timed tasks

class TaskManager:
    #initializes the UI, still no drop down etc.
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


    #checks if database.csv file is present in the ToDoList.py directory
    #if it isn't it makes the file with the keys/paramenters that the tasks are going to use
    #if the file is present in the same directory, skips over and proceeds to use that file
    def create_file(self):
        if not os.path.isfile("database.csv"):
            with open('database.csv', 'w', newline='') as csvfile:
                fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    #used for write2file so that it every task has different ID so it can be specifically called/pointed to
    #gets the id of the last task so that the next can be incremented
    def get_last_task_id(self):
        if os.path.isfile("database.csv"):
            with open('database.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                tasks = list(reader)
                if tasks:
                    last_task = tasks[-1]
                    return int(last_task['task_id'])
        return 0


    #most is UI implementation in a new window, still need to pass verification of input ex. if date is valid format
    #when that is done it should open a pop up window saying to input that info again
    #updates the list/shows with new task, when the submit button is closed (in the command)
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

    #gets the information that was inputed in new_task as writes it to the file
    #assigns the newly created task a new task id so it wont get mistaken/edited for another task
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


    #removes the task that is highlighted/clicked on in the tkinter GUI window
    #updates the list after it's removed
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


    #similar to new_task but adds the option to rewrite/edit a clicked on + selected task
    #GUI is the same as new_task, updates at the end with update_task
    #very similar to new_task with the update
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

    #used with edit_task
    #rewrites the given task id's information in the csv file with the updated information from edit_task
    #instead of using the incremented task id like new_task, it instead checks if it matches before doing any work
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

    #shows the tasks with the format on task_id name description - DueL date time     priority: priority
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


    #GUI created, new window with date ascending+descending options
    #still need to complete
    def sort_by(self):
        sort_window = tk.Toplevel(self.master)
        sort_window.title("Sort By")

        btn_descending = tk.Button(sort_window, text="Descending Date")
        btn_descending.pack()
        btn_ascending = tk.Button(sort_window, text="Ascending Date")
        btn_ascending.pack()
    #in progress
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
