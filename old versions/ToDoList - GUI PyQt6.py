# # import sys
# # from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel
# # import schedule as s
# # import datetime as dt
# # import ToDoListFunctions
# #
# # class ToDoListApp(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.setWindowTitle("To-Do List App")
# #         self.resize(400, 300)
# #
# #         self.tasks = []
# #
# #         self.layout = QVBoxLayout()
# #
# #         self.task_input = QLineEdit()
# #         self.add_button = QPushButton("Add Task")
# #         self.add_button.clicked.connect(self.add_task)
# #
# #         self.task_list = QListWidget()
# #
# #         self.delete_button = QPushButton("Delete Task")
# #         self.delete_button.clicked.connect(self.delete_task)
# #
# #         self.layout.addWidget(QLabel("Add Task:"))
# #         self.layout.addWidget(self.task_input)
# #         self.layout.addWidget(self.add_button)
# #         self.layout.addWidget(QLabel("Tasks:"))
# #         self.layout.addWidget(self.task_list)
# #         self.layout.addWidget(self.delete_button)
# #
# #         self.setLayout(self.layout)
# #
# #     def add_task(self):
# #         task_text = self.task_input.text()
# #         if task_text:
# #             self.tasks.append(task_text)
# #             self.task_list.addItem(task_text)
# #             self.task_input.clear()
# #
# #     def delete_task(self):
# #         selected_items = self.task_list.selectedItems()
# #         if selected_items:
# #             for item in selected_items:
# #                 self.task_list.takeItem(self.task_list.row(item))
# #                 self.tasks.remove(item.text())
# #
# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     todo_app = ToDoListApp()
# #     todo_app.show()
# #     sys.exit(app.exec())
# import csv
# import os
# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
#
# class TaskManager(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Task Manager")
#         self.setGeometry(100, 100, 700, 500)
#
#         self.create_file()
#
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         main_layout = QHBoxLayout(central_widget)
#
#         self.options_widget = QWidget()
#         main_layout.addWidget(self.options_widget)
#
#         self.list_widget = QListWidget()
#         main_layout.addWidget(self.list_widget)
#
#         self.label = QLabel("TO DO")
#         font = self.label.font()
#         font.setFamily("Helvetica")
#         self.label.setFont(font)
#         self.options_layout = QVBoxLayout(self.options_widget)
#         self.options_layout.addWidget(self.label)
#
#         self.new_task_button = QPushButton("Create New Task")
#         self.new_task_button.clicked.connect(self.new_task)
#         self.options_layout.addWidget(self.new_task_button)
#
#         self.delete_task_button = QPushButton("Delete Task")
#         self.delete_task_button.clicked.connect(self.delete_task)
#         self.options_layout.addWidget(self.delete_task_button)
#
#         self.edit_task_button = QPushButton("Edit Task")
#         self.edit_task_button.clicked.connect(self.edit_task)
#         self.options_layout.addWidget(self.edit_task_button)
#
#         self.sort_button = QPushButton("Sort By")
#         self.sort_button.clicked.connect(self.sort_by)
#         self.options_layout.addWidget(self.sort_button)
#
#         self.group_button = QPushButton("Group By")
#         self.group_button.clicked.connect(self.group_by)
#         self.options_layout.addWidget(self.group_button)
#
#         self.show_tasks()
#
#     def create_file(self):
#         if not os.path.isfile("database.csv"):
#             with open('database.csv', 'w', newline='') as csvfile:
#                 fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 writer.writeheader()
#
#     def get_last_task_id(self):
#         if os.path.isfile("database.csv"):
#             with open('database.csv', 'r') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 tasks = list(reader)
#                 if tasks:
#                     last_task = tasks[-1]
#                     return int(last_task['task_id'])
#         return 0
#
#     def new_task(self):
#         self.new_window = QWidget()
#         self.new_window.setWindowTitle("New Task")
#         layout = QVBoxLayout(self.new_window)
#
#         self.name_label = QLabel("Name:")
#         layout.addWidget(self.name_label)
#         self.name_entry = QLineEdit()
#         layout.addWidget(self.name_entry)
#
#         self.description_label = QLabel("Description:")
#         layout.addWidget(self.description_label)
#         self.description_entry = QLineEdit()
#         layout.addWidget(self.description_entry)
#
#         self.date_label = QLabel("Date (MM/DD/YY):")
#         layout.addWidget(self.date_label)
#         self.date_entry = QLineEdit()
#         layout.addWidget(self.date_entry)
#
#         self.time_label = QLabel("Time (HH:MM AM/PM):")
#         layout.addWidget(self.time_label)
#         self.time_entry = QLineEdit()
#         layout.addWidget(self.time_entry)
#
#         self.interval_label = QLabel("Interval:")
#         layout.addWidget(self.interval_label)
#         self.interval_entry = QLineEdit()
#         layout.addWidget(self.interval_entry)
#
#         self.priority_label = QLabel("Priority:")
#         layout.addWidget(self.priority_label)
#         self.priority_entry = QLineEdit()
#         layout.addWidget(self.priority_entry)
#
#         self.submit_button = QPushButton("Submit")
#         self.submit_button.clicked.connect(self.write2file)
#         layout.addWidget(self.submit_button)
#
#         self.new_window.show()
#
#     def write2file(self):
#         name = self.name_entry.text()
#         description = self.description_entry.text()
#         date = self.date_entry.text()
#         time = self.time_entry.text()
#         interval = self.interval_entry.text()
#         priority = self.priority_entry.text()
#
#         last_task_id = self.get_last_task_id()
#         next_task_id = last_task_id + 1
#
#         with open('database.csv', 'a', newline='') as csvfile:
#             fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#             writer.writerow({
#                 'task_id': next_task_id,
#                 'Names': name,
#                 'Descriptions': description,
#                 'Dates': date,
#                 'Times': time,
#                 'Interval': interval,
#                 'Priority': priority
#             })
#
#         self.new_window.close()
#         self.show_tasks()
#
#     def delete_task(self):
#         selected_task_item = self.list_widget.currentItem()
#         if selected_task_item:
#             task_id = int(selected_task_item.text().split(':')[0])
#             with open('database.csv', 'r') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 rows = [row for row in reader if int(row['task_id']) != task_id]
#
#             with open('database.csv', 'w', newline='') as csvfile:
#                 fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 writer.writerows(rows)
#
#             self.show_tasks()
#
#     def edit_task(self):
#         selected_task_item = self.list_widget.currentItem()
#         if selected_task_item:
#             task_id = int(selected_task_item.text().split(':')[0])
#
#             with open('database.csv', 'r') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for task in reader:
#                     if int(task['task_id']) == task_id:
#                         self.new_window = QWidget()
#                         self.new_window.setWindowTitle("Edit Task")
#                         layout = QVBoxLayout(self.new_window)
#
#                         self.name_label = QLabel("Name:")
#                         layout.addWidget(self.name_label)
#                         self.name_entry = QLineEdit()
#                         self.name_entry.setText(task['Names'])
#                         layout.addWidget(self.name_entry)
#
#                         self.description_label = QLabel("Description:")
#                         layout.addWidget(self.description_label)
#                         self.description_entry = QLineEdit()
#                         self.description_entry.setText(task['Descriptions'])
#                         layout.addWidget(self.description_entry)
#
#                         self.date_label = QLabel("Date (MM/DD/YY):")
#                         layout.addWidget(self.date_label)
#                         self.date_entry = QLineEdit()
#                         self.date_entry.setText(task['Dates'])
#                         layout.addWidget(self.date_entry)
#
#                         self.time_label = QLabel("Time (HH:MM AM/PM):")
#                         layout.addWidget(self.time_label)
#                         self.time_entry = QLineEdit()
#                         self.time_entry.setText(task['Times'])
#                         layout.addWidget(self.time_entry)
#
#                         self.interval_label = QLabel("Interval:")
#                         layout.addWidget(self.interval_label)
#                         self.interval_entry = QLineEdit()
#                         self.interval_entry.setText(task['Interval'])
#                         layout.addWidget(self.interval_entry)
#
#                         self.priority_label = QLabel("Priority:")
#                         layout.addWidget(self.priority_label)
#                         self.priority_entry = QLineEdit()
#                         self.priority_entry.setText(task['Priority'])
#                         layout.addWidget(self.priority_entry)
#
#                         self.submit_button = QPushButton("Submit")
#                         self.submit_button.clicked.connect(lambda _, id=task_id: self.update_task(id))
#                         layout.addWidget(self.submit_button)
#
#                         self.new_window.show()
#                         break
#
#     def update_task(self, task_id):
#         name = self.name_entry.text()
#         description = self.description_entry.text()
#         date = self.date_entry.text()
#         time = self.time_entry.text()
#         interval = self.interval_entry.text()
#         priority = self.priority_entry.text()
#
#         with open('database.csv', 'r') as csvfile:
#             reader = csv.DictReader(csvfile)
#             rows = [row if int(row['task_id']) != task_id else {
#                 'task_id': task_id,
#                 'Names': name,
#                 'Descriptions': description,
#                 'Dates': date,
#                 'Times': time,
#                 'Interval': interval,
#                 'Priority': priority
#             } for row in reader]
#
#         with open('database.csv', 'w', newline='') as csvfile:
#             fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Interval', 'Priority']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(rows)
#
#         self.new_window.close()
#         self.show_tasks()
#
#     def show_tasks(self):
#         self.list_widget.clear()
#         if os.path.isfile("database.csv"):
#             with open('database.csv', 'r') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for task in reader:
#                     task_info = f"{task['task_id']}: {task['Names']} {task['Descriptions']} - Due: {task['Dates']} {task['Times']}    Priority:{task['Priority']}"
#                     self.list_widget.addItem(task_info)
#         else:
#             self.list_widget.addItem("No tasks found.")
#
#     def sort_by(self):
#         sort_msg_box = QMessageBox()
#         sort_msg_box.setText("Functionality for sorting is not implemented yet.")
#         sort_msg_box.exec()
#
#     def group_by(self):
#         group_msg_box = QMessageBox()
#         group_msg_box.setText("Functionality for grouping is not implemented yet.")
#         group_msg_box.exec()
#
# def main():
#     app = QApplication([])
#     task_manager = TaskManager()
#     task_manager.show()
#     app.exec()
#
# if __name__ == "__main__":
#     main()

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
import