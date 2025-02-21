import csv
import os
from PyQt6 import QtWidgets, QtCore


class ToDoList:
    def __init__(self):
        super().__init__()
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
    def valid_input(self, task, desc, date, time, inter, prio):
        current_date = QtCore.QDate.currentDate()
        valid_intervals = ["daily", "hourly", "weekly", "none"]
        valid_priorities = ["high", "low", "medium", "none"]

        task_text = task.toPlainText().lower().strip()
        desc_text = desc.toPlainText().lower().strip()
        date_value = date.date().toPyDate()
        time_value = time.time().toString("HH:mm")
        inter_text = inter.toPlainText().lower().strip()
        prio_text = prio.toPlainText().lower().strip()

        if date_value < current_date:
            self.show_error_message("Invalid Date", "Please choose a date after the current date.")
            return False
        elif inter_text.lower() not in valid_intervals:
            self.show_error_message("Invalid Interval", "Please choose a valid interval: daily, hourly, weekly, or none.")
            return False
        elif prio_text.lower() not in valid_priorities:
            self.show_error_message("Invalid Priority", "Please choose a valid priority: high, low, medium, or none.")
            return False
        else:
            last_task_id = self.get_last_task_id()
            next_task_id = last_task_id + 1
            with open('database.csv', 'a', newline='') as csvfile:
                fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'task_id': next_task_id,
                    'Names': task_text,
                    'Descriptions': desc_text,
                    'Dates': date_value,
                    'Times': time_value,
                    'Interval': inter_text,
                    'Priority': prio_text
                })
            return True

    def show_error_message(self, title, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec()

    def delete_task(self, task_id):
        try:
            with open("database.csv", 'r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

            if task_id < 0 or task_id >= len(rows):
                print("Index out of range.")
                return

            # Deleting columns B to G (index 1 to 6) of the selected row
            del rows[task_id][1:7]

            with open("database.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        except Exception as e:
            print("An error occurred:", str(e))


    def edit_task(self, index, task, desc, date, time, inter, prio):
        current_date = QtCore.QDate.currentDate()
        valid_intervals = ["daily", "hourly", "weekly", "none"]
        valid_priorities = ["high", "low", "medium", "none"]

        task_text = task.toPlainText().lower().strip()
        desc_text = desc.toPlainText().lower().strip()
        date_value = date.date().toPyDate()
        time_value = time.time().toString("HH:mm")
        inter_text = inter.toPlainText().lower().strip()
        prio_text = prio.toPlainText().lower().strip()

        if date_value < current_date:
            self.show_error_message("Invalid Date", "Please choose a date after the current date.")
            return False
        elif inter_text.lower() not in valid_intervals:
            self.show_error_message("Invalid Interval",
                                    "Please choose a valid interval: daily, hourly, weekly, or none.")
            return False
        elif prio_text.lower() not in valid_priorities:
            self.show_error_message("Invalid Priority", "Please choose a valid priority: high, low, medium, or none.")
            return False
        else:
            rows = []  # To store all rows
            with open('database.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    rows.append(row)
            # Update the row with the new information
            for row in rows:
                if int(row['task_id']) == index:
                    row.update({
                        'Names': task_text,
                        'Descriptions': desc_text,
                        'Dates': date_value,
                        'Times': time_value,
                        'Interval': inter_text,
                        'Priority': prio_text
                    })
                    break  # Stop searching once the row is updated

            # Rewrite the entire file with the updated data
            with open('database.csv', 'w', newline='') as csvfile:
                fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            return True

    def update_task(self, task_id, name, description, date, time, interval, priority):
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



