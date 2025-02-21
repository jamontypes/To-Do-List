""""
# orange : #f6be5d
# task box: #dddddd
# text : #1d1d1d
# create task section : #ffffff
# to do list section : #f0f0f0
# delete / edit buttons : #b7b7b7
"""""

import sys
import csv
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from ToDoListFunctions import ToDoList


class ToDoListWindow(object):
    def __init__(self):
        ToDoList().create_file()
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("PriorityBtn")
        mainwindow.resize(807, 613)
        #central widget
        self.centralwidget = QtWidgets.QWidget(parent=mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #ffffff;")

        #task button ui
        self.CreateTask = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CreateTask.setGeometry(QtCore.QRect(25, 30, 230, 68))
        self.CreateTask.setStyleSheet("border-radius: 5x;")
        self.CreateTask.setObjectName("CreateTask")

        taskbtn_img = "icons/NewTaskButton.png"
        taskbtn = QPixmap(taskbtn_img)
        self.CreateTask.setIcon(QIcon(taskbtn))
        self.CreateTask.setIconSize(taskbtn.size())

        scaled_pixmap = taskbtn.scaled(300, 300)
        self.CreateTask.setIcon(QIcon(scaled_pixmap))
        self.CreateTask.setIconSize(scaled_pixmap.size())
        #going to later changed to open a new window
        self.CreateTask.clicked.connect(self.open_create_task_window)


        #section where tasks are
        self.TaskSection = QtWidgets.QFrame(parent=self.centralwidget)
        self.TaskSection.setGeometry(QtCore.QRect(289, 0, 521, 631))
        self.TaskSection.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TaskSection.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TaskSection.setObjectName("TaskSection")
        self.TaskSection.setStyleSheet("background-color: #f0f0f0;")

        #area of tasks
        self.TaskLabel_2 = QtWidgets.QWidget(parent=self.TaskSection)
        self.TaskLabel_2.setGeometry(QtCore.QRect(10, 120, 495, 480))
        self.TaskLabel_2.setStyleSheet("background-color: #dddddd;")

        #circle buttons
        cirbtn_img1 = "icons/unchecked.png"
        cirbtn1 = QtGui.QPixmap(cirbtn_img1)
        scaled_cir1 = cirbtn1.scaled(20, 20)
        self.click1status = False

        self.CircleButton_1 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_1.setGeometry(QtCore.QRect(30, 40, 31, 24))
        self.CircleButton_1.setStyleSheet("border-radius: 5px;")
        self.CircleButton_1.setIcon(QtGui.QIcon(scaled_cir1))
        self.CircleButton_1.setIconSize(scaled_cir1.size())
        self.CircleButton_1.clicked.connect(lambda: self.toggle_button_icon(1))

        cirbtn_img2 = "icons/unchecked.png"
        cirbtn2 = QtGui.QPixmap(cirbtn_img2)
        scaled_cir2 = cirbtn2.scaled(20, 20)
        self.click2status = False

        self.CircleButton_2 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_2.setGeometry(QtCore.QRect(30, 100, 31, 24))
        self.CircleButton_2.setStyleSheet("border-radius: 5x;")
        self.CircleButton_2.setIcon(QIcon(scaled_cir2))
        self.CircleButton_2.setIconSize(scaled_cir2.size())
        self.CircleButton_2.clicked.connect(lambda: self.toggle_button_icon(2))

        cirbtn_img3 = "icons/unchecked.png"
        cirbtn3 = QtGui.QPixmap(cirbtn_img3)
        scaled_cir3 = cirbtn3.scaled(20, 20)
        self.click3status = False

        self.CircleButton_3 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_3.setGeometry(QtCore.QRect(30, 160, 31, 24))
        self.CircleButton_3.setStyleSheet("border-radius: 5x;")
        self.CircleButton_3.setIcon(QIcon(scaled_cir3))
        self.CircleButton_3.setIconSize(scaled_cir3.size())
        self.CircleButton_3.clicked.connect(lambda: self.toggle_button_icon(3))

        cirbtn_img4 = "icons/unchecked.png"
        cirbtn4 = QtGui.QPixmap(cirbtn_img4)
        scaled_cir4 = cirbtn4.scaled(20, 20)
        self.click4status = False

        self.CircleButton_4 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_4.setGeometry(QtCore.QRect(30, 220, 31, 24))
        self.CircleButton_4.setStyleSheet("border-radius: 5x;")
        self.CircleButton_4.setIcon(QIcon(scaled_cir4))
        self.CircleButton_4.setIconSize(scaled_cir4.size())
        self.CircleButton_4.clicked.connect(lambda: self.toggle_button_icon(4))

        cirbtn_img5 = "icons/unchecked.png"
        cirbtn5 = QtGui.QPixmap(cirbtn_img5)
        scaled_cir5 = cirbtn5.scaled(20, 20)
        self.click5status = False

        self.CircleButton_5 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_5.setGeometry(QtCore.QRect(30, 280, 31, 24))
        self.CircleButton_5.setStyleSheet("border-radius: 5x;")
        self.CircleButton_5.setIcon(QIcon(scaled_cir5))
        self.CircleButton_5.setIconSize(scaled_cir5.size())
        self.CircleButton_5.clicked.connect(lambda: self.toggle_button_icon(5))

        cirbtn_img6 = "icons/unchecked.png"
        cirbtn6 = QtGui.QPixmap(cirbtn_img6)
        scaled_cir6 = cirbtn6.scaled(20, 20)
        self.click6status = False

        self.CircleButton_6 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_6.setGeometry(QtCore.QRect(30, 340, 31, 24))
        self.CircleButton_6.setStyleSheet("border-radius: 5x;")
        self.CircleButton_6.setIcon(QIcon(scaled_cir6))
        self.CircleButton_6.setIconSize(scaled_cir6.size())
        self.CircleButton_6.clicked.connect(lambda: self.toggle_button_icon(6))

        cirbtn_img7 = "icons/unchecked.png"
        cirbtn7 = QtGui.QPixmap(cirbtn_img7)
        scaled_cir7 = cirbtn4.scaled(20, 20)
        self.click7status = False

        self.CircleButton_7 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.CircleButton_7.setGeometry(QtCore.QRect(30, 400, 31, 24))
        self.CircleButton_7.setStyleSheet("border-radius: 5x;")
        self.CircleButton_7.setIcon(QIcon(scaled_cir7))
        self.CircleButton_7.setIconSize(scaled_cir7.size())
        self.CircleButton_7.clicked.connect(lambda: self.toggle_button_icon(7))

        #task labels
        self.TaskLabel = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.TaskLabel.setGeometry(QtCore.QRect(80, 40, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.TaskLabel.setFont(font)
        self.label_2 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.TaskLabel_3 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.TaskLabel_3.setGeometry(QtCore.QRect(80, 160, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.TaskLabel_3.setFont(font)
        self.TaskLabel_4 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.TaskLabel_4.setGeometry(QtCore.QRect(80, 220, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.TaskLabel_4.setFont(font)
        self.TaskLabel_5 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.TaskLabel_5.setGeometry(QtCore.QRect(80, 280, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.TaskLabel_5.setFont(font)
        self.TaskLabel_6 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.TaskLabel_6.setGeometry(QtCore.QRect(80, 340, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.TaskLabel_6.setFont(font)
        self.TaskLabel_7 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.TaskLabel_7.setGeometry(QtCore.QRect(80, 400, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.TaskLabel_7.setFont(font)

        #delete buttons
        trashbtn_img = "icons/trash.png"
        trashbtn = QPixmap(trashbtn_img)
        scaled_trash = trashbtn.scaled(20, 20)

        self.DeleteButton = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton.setGeometry(QtCore.QRect(425, 40, 31, 24))
        self.DeleteButton.setStyleSheet("border-radius: 5x;")
        self.DeleteButton.setIcon(QIcon(scaled_trash))
        self.DeleteButton.setIconSize(scaled_trash.size())
        # self.DeleteButton.clicked.connect(lambda: ToDoList.delete_task(task_id=1))
        self.DeleteButton.clicked.connect(lambda: ToDoList().delete_task(1))


        self.DeleteButton_2 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton_2.setGeometry(QtCore.QRect(425, 100, 31, 24))
        self.DeleteButton_2.setStyleSheet("border-radius: 5x;")
        self.DeleteButton_2.setIcon(QIcon(scaled_trash))
        self.DeleteButton_2.setIconSize(scaled_trash.size())
        self.DeleteButton_2.clicked.connect(lambda: ToDoList().delete_task(2))

        self.DeleteButton_3 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton_3.setGeometry(QtCore.QRect(425, 160, 31, 24))
        self.DeleteButton_3.setStyleSheet("border-radius: 5x;")
        self.DeleteButton_3.setIcon(QIcon(scaled_trash))
        self.DeleteButton_3.setIconSize(scaled_trash.size())
        self.DeleteButton_3.clicked.connect(lambda: ToDoList().delete_task(3))

        self.DeleteButton_4 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton_4.setGeometry(QtCore.QRect(425, 220, 31, 24))
        self.DeleteButton_4.setStyleSheet("border-radius: 5x;")
        self.DeleteButton_4.setIcon(QIcon(scaled_trash))
        self.DeleteButton_4.setIconSize(scaled_trash.size())
        self.DeleteButton_4.clicked.connect(lambda: ToDoList().delete_task(4))

        self.DeleteButton_5 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton_5.setGeometry(QtCore.QRect(425, 280, 31, 24))
        self.DeleteButton_5.setStyleSheet("border-radius: 5x;")
        self.DeleteButton_5.setIcon(QIcon(scaled_trash))
        self.DeleteButton_5.setIconSize(scaled_trash.size())
        self.DeleteButton_5.clicked.connect(lambda: ToDoList().delete_task(5))

        self.DeleteButton_6 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton_6.setGeometry(QtCore.QRect(425, 340, 31, 24))
        self.DeleteButton_6.setStyleSheet("border-radius: 5x;")
        self.DeleteButton_6.setIcon(QIcon(scaled_trash))
        self.DeleteButton_6.setIconSize(scaled_trash.size())
        self.DeleteButton_6.clicked.connect(lambda: ToDoList().delete_task(6))

        self.DeleteButton_7 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.DeleteButton_7.setGeometry(QtCore.QRect(425, 400, 31, 24))
        self.DeleteButton_7.setStyleSheet("border-radius: 5x;")
        self.DeleteButton_7.setIcon(QIcon(scaled_trash))
        self.DeleteButton_7.setIconSize(scaled_trash.size())
        self.DeleteButton_7.clicked.connect(lambda: ToDoList().delete_task(7))

        #edit buttons
        editbtn_img = "icons/edit.png"
        editbtn = QPixmap(editbtn_img)
        scaled_edit = editbtn.scaled(20, 20)

        self.editButton = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton.setGeometry(QtCore.QRect(390, 40, 31, 24))
        self.editButton.setStyleSheet("border-radius: 5x;")
        self.editButton.setIcon(QIcon(scaled_edit))
        self.editButton.setIconSize(scaled_edit.size())
        self.editButton.clicked.connect(lambda: self.open_edit_task_window(1))

        self.editButton_2 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton_2.setGeometry(QtCore.QRect(390, 100, 31, 24))
        self.editButton_2.setStyleSheet("border-radius: 5x;")
        self.editButton_2.setIcon(QIcon(scaled_edit))
        self.editButton_2.setIconSize(scaled_edit.size())
        self.editButton_2.clicked.connect(lambda: self.open_edit_task_window(2))

        self.editButton_3 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton_3.setGeometry(QtCore.QRect(390, 160, 31, 24))
        self.editButton_3.setStyleSheet("border-radius: 5x;")
        self.editButton_3.setIcon(QIcon(scaled_edit))
        self.editButton_3.setIconSize(scaled_edit.size())
        self.editButton_3.clicked.connect(lambda: self.open_edit_task_window(3))

        self.editButton_4 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton_4.setGeometry(QtCore.QRect(390, 220, 31, 24))
        self.editButton_4.setStyleSheet("border-radius: 5x;")
        self.editButton_4.setIcon(QIcon(scaled_edit))
        self.editButton_4.setIconSize(scaled_edit.size())
        self.editButton_4.clicked.connect(lambda: self.open_edit_task_window(4))

        self.editButton_5 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton_5.setGeometry(QtCore.QRect(390, 280, 31, 24))
        self.editButton_5.setStyleSheet("border-radius: 5x;")
        self.editButton_5.setIcon(QIcon(scaled_edit))
        self.editButton_5.setIconSize(scaled_edit.size())
        self.editButton_5.clicked.connect(lambda: self.open_edit_task_window(5))

        self.editButton_6 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton_6.setGeometry(QtCore.QRect(390, 340, 31, 24))
        self.editButton_6.setStyleSheet("border-radius: 5x;")
        self.editButton_6.setIcon(QIcon(scaled_edit))
        self.editButton_6.setIconSize(scaled_edit.size())
        self.editButton_6.clicked.connect(lambda: self.open_edit_task_window(6))

        self.editButton_7 = QtWidgets.QPushButton(parent=self.TaskLabel_2)
        self.editButton_7.setGeometry(QtCore.QRect(390, 400, 31, 24))
        self.editButton_7.setStyleSheet("border-radius: 5x;")
        self.editButton_7.setIcon(QIcon(scaled_edit))
        self.editButton_7.setIconSize(scaled_edit.size())
        self.editButton_7.clicked.connect(lambda: self.open_edit_task_window(7))

        #date buttons
        self.datelabel = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel.setGeometry(QtCore.QRect(320, 50, 49, 16))
        self.datelabel_2 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel_2.setGeometry(QtCore.QRect(320, 110, 49, 16))
        self.datelabel_3 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel_3.setGeometry(QtCore.QRect(320, 170, 49, 16))
        self.datelabel_4 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel_4.setGeometry(QtCore.QRect(320, 230, 49, 16))
        self.datelabel_5 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel_5.setGeometry(QtCore.QRect(320, 290, 49, 16))
        self.datelabel_6 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel_6.setGeometry(QtCore.QRect(320, 350, 49, 16))
        self.datelabel_7 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.datelabel_7.setGeometry(QtCore.QRect(320, 410, 49, 16))

        #time labels
        self.timelabel = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel.setGeometry(QtCore.QRect(320, 35, 49, 16))
        self.timelabel_2 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel_2.setGeometry(QtCore.QRect(320, 95, 49, 16))
        self.timelabel_3 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel_3.setGeometry(QtCore.QRect(320, 155, 49, 16))
        self.timelabel_4 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel_4.setGeometry(QtCore.QRect(320, 215, 49, 16))
        self.timelabel_5 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel_5.setGeometry(QtCore.QRect(320, 275, 49, 16))
        self.timelabel_6 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel_6.setGeometry(QtCore.QRect(320, 335, 49, 16))
        self.timelabel_7 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.timelabel_7.setGeometry(QtCore.QRect(320, 395, 49, 16))

        #description labels
        self.descriptionlabel = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel.setGeometry(QtCore.QRect(210, 40, 91, 16))
        self.descriptionlabel_2 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel_2.setGeometry(QtCore.QRect(210, 100, 91, 16))
        self.descriptionlabel_3 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel_3.setGeometry(QtCore.QRect(210, 160, 91, 16))
        self.descriptionlabel_4 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel_4.setGeometry(QtCore.QRect(210, 220, 91, 16))
        self.descriptionlabel_5 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel_5.setGeometry(QtCore.QRect(210, 280, 91, 16))
        self.descriptionlabel_6 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel_6.setGeometry(QtCore.QRect(210, 340, 91, 16))
        self.descriptionlabel_7 = QtWidgets.QLabel(parent=self.TaskLabel_2)
        self.descriptionlabel_7.setGeometry(QtCore.QRect(210, 400, 91, 16))

        #main text "TO DO LIST"
        self.ToDoLabel = QtWidgets.QLabel(parent=self.TaskSection)
        self.ToDoLabel.setGeometry(QtCore.QRect(50, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.ToDoLabel.setFont(font)
        self.ToDoLabel.setObjectName("ToDoLabel")

        #sort by text
        self.SortBy = QtWidgets.QLabel(parent=self.centralwidget)
        self.SortBy.setGeometry(QtCore.QRect(20, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SortBy.setFont(font)
        self.SortBy.setObjectName("SortBy")

        #group by text
        self.GroupBy = QtWidgets.QLabel(parent=self.centralwidget)
        self.GroupBy.setGeometry(QtCore.QRect(20, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.GroupBy.setFont(font)
        self.GroupBy.setObjectName("GroupBy")

        #priority button - same as date button
        self.PriorityBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PriorityBtn.setGeometry(QtCore.QRect(210, 155, 30, 30))
        self.PriorityBtn.setObjectName("PriorityBtn_2")
        mainwindow.setCentralWidget(self.centralwidget)

        self.PriorityBtn.setStyleSheet("border-radius: 5x;")
        self.PriorityBtn.setObjectName("PriorityBtn")

        priobtn_img = "icons/UpArrow.png"
        priobtn = QPixmap(priobtn_img)
        self.PriorityBtn.setIcon(QIcon(priobtn))
        self.PriorityBtn.setIconSize(priobtn.size())

        scaled_pixmap_datebtn = priobtn.scaled(20, 20)
        self.PriorityBtn.setIcon(QIcon(scaled_pixmap_datebtn))
        self.PriorityBtn.setIconSize(scaled_pixmap_datebtn.size())
        self.PriorityBtn.clicked.connect(self.sort_csv_by_priority)


        #ui translation
        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

        #date button - with picture flip + organization function ------------------------
        self.DateBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DateBtn.setGeometry(QtCore.QRect(210, 122, 30, 30))
        self.DateBtn.setObjectName("DateBtn")
        self.DateBtn.setStyleSheet("border-radius: 5px;")
        self.DateBtn.setProperty("sort_order", "descending")  # Set default sort order
        self.set_date_button_icon("icons/DownArrow.png")

        self.DateBtn.clicked.connect(self.sort_csv_by_date)

    def sort_csv_by_date(self):
        try:
            with open('database.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                if 'Dates' not in reader.fieldnames:
                    print("Error: 'Date' column not found in CSV file.")
                    return  # Exit the function if 'Date' column is missing

                data = list(reader)

            # Toggle sort order
            sort_order = self.DateBtn.property("sort_order")
            if sort_order == "ascending":
                sorted_data = sorted(data, key=lambda x: x['Dates'])
                self.DateBtn.setProperty("sort_order", "descending")
                self.set_date_button_icon("icons/DownArrow.png")
            else:
                sorted_data = sorted(data, key=lambda x: x['Dates'], reverse=True)
                self.DateBtn.setProperty("sort_order", "ascending")
                self.set_date_button_icon("icons/UpArrow.png")

            # Write sorted data back to CSV file
            with open('database.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(sorted_data)
        except Exception as e:
            print(f"An error occurred: {e}")

        self.retranslateUi(PriorityBtn)

    def sort_csv_by_priority(self):
        try:
            with open('database.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                if 'Priority' not in reader.fieldnames:
                    print("Error: 'Priority' column not found in CSV file.")
                    return

                data = list(reader)

            sort_order = self.PriorityBtn.property("sort_order")
            if sort_order == "ascending":
                sorted_data = sorted(data,
                                     key=lambda x: {"high": 0, "medium": 1, "low": 2, "none": 3}.get(x['Priority'], 4))
                self.PriorityBtn.setProperty("sort_order", "descending")
                self.set_prio_button_icon("icons/DownArrow.png")
            else:
                sorted_data = sorted(data,
                                     key=lambda x: {"high": 0, "medium": 1, "low": 2, "none": 3}.get(x['Priority'], 4),
                                     reverse=True)
                self.PriorityBtn.setProperty("sort_order", "ascending")
                self.set_prio_button_icon("icons/UpArrow.png")

            with open('database.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(sorted_data)
        except Exception as e:
            print(f"An error occurred: {e}")

        self.retranslateUi(PriorityBtn)



    def set_date_button_icon(self, icon_path):
        datebtn = QtGui.QPixmap(icon_path)
        scaled_pixmap_datebtn = datebtn.scaled(20, 20)
        self.DateBtn.setIcon(QtGui.QIcon(scaled_pixmap_datebtn))
        self.DateBtn.setIconSize(scaled_pixmap_datebtn.size())
        self.retranslateUi(PriorityBtn)


    def set_prio_button_icon(self, icon_path):
        priobtn = QtGui.QPixmap(icon_path)
        scaled_pixmap_priobtn = priobtn.scaled(20, 20)
        self.PriorityBtn.setIcon(QtGui.QIcon(scaled_pixmap_priobtn))

    def toggle_button_icon(self, button_num):
        button = None
        status = None
        if button_num == 1:
            button = self.CircleButton_1
            status = self.click1status
        elif button_num == 2:
            button = self.CircleButton_2
            status = self.click2status
        elif button_num == 3:
            button = self.CircleButton_3
            status = self.click3status
        elif button_num == 4:
            button = self.CircleButton_4
            status = self.click4status
        elif button_num == 5:
            button = self.CircleButton_5
            status = self.click5status
        elif button_num == 6:
            button = self.CircleButton_6
            status = self.click6status
        elif button_num == 7:
            button = self.CircleButton_7
            status = self.click7status

        if status:
            button.setIcon(QtGui.QIcon("icons/unchecked.png"))
        else:
            button.setIcon(QtGui.QIcon("icons/checked.png"))

        if button_num == 1:
            self.click1status = not self.click1status
        elif button_num == 2:
            self.click2status = not self.click2status
        elif button_num == 3:
            self.click3status = not self.click3status
        elif button_num == 4:
            self.click4status = not self.click4status
        elif button_num == 5:
            self.click5status = not self.click5status
        elif button_num == 6:
            self.click6status = not self.click6status
        elif button_num == 7:
            self.click7status = not self.click7status
    def retranslateUi(self, PriorityBtn):

        _translate = QtCore.QCoreApplication.translate
        PriorityBtn.setWindowTitle(_translate("PriorityBtn", "MainWindow"))

        self.ToDoLabel.setText(_translate("PriorityBtn", "TO DO"))
        self.SortBy.setText(_translate("PriorityBtn", "Sort by             Date"))
        self.GroupBy.setText(_translate("PriorityBtn", "Group by     Priority"))

        self.ToDoLabel.setText(_translate("PriorityBtn", "TO DO"))

        with open('database.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            names_list = []
            dates_list = []
            times_list = []
            descriptions_list = []
            for i, row in enumerate(reader, start=2):
                if i > 8:
                    break
                names_list.append(row['Names'])
                dates_list.append(row['Dates'])
                times_list.append(row['Times'])
                descriptions_list.append(row['Descriptions'])

        self.TaskLabel.setText(_translate("PriorityBtn", names_list[0]))
        self.datelabel.setText(_translate("PriorityBtn", dates_list[0]))
        self.timelabel.setText(_translate("PriorityBtn", times_list[0]))
        self.descriptionlabel.setText(_translate("PriorityBtn", descriptions_list[0]))

        self.label_2.setText(_translate("PriorityBtn", names_list[1]))
        self.datelabel_2.setText(_translate("PriorityBtn", dates_list[1]))
        self.timelabel_2.setText(_translate("PriorityBtn", times_list[1]))
        self.descriptionlabel_2.setText(_translate("PriorityBtn", descriptions_list[1]))

        self.TaskLabel_3.setText(_translate("PriorityBtn", names_list[2]))
        self.datelabel_3.setText(_translate("PriorityBtn", dates_list[2]))
        self.timelabel_3.setText(_translate("PriorityBtn", times_list[2]))
        self.descriptionlabel_3.setText(_translate("PriorityBtn", descriptions_list[2]))

        self.TaskLabel_4.setText(_translate("PriorityBtn", names_list[3]))
        self.datelabel_4.setText(_translate("PriorityBtn", dates_list[3]))
        self.timelabel_4.setText(_translate("PriorityBtn", times_list[3]))
        self.descriptionlabel_4.setText(_translate("PriorityBtn", descriptions_list[3]))

        self.TaskLabel_5.setText(_translate("PriorityBtn", names_list[4]))
        self.datelabel_5.setText(_translate("PriorityBtn", dates_list[4]))
        self.timelabel_5.setText(_translate("PriorityBtn", times_list[4]))
        self.descriptionlabel_5.setText(_translate("PriorityBtn", descriptions_list[4]))

        self.TaskLabel_6.setText(_translate("PriorityBtn", names_list[5]))
        self.datelabel_6.setText(_translate("PriorityBtn", dates_list[5]))
        self.timelabel_6.setText(_translate("PriorityBtn", times_list[5]))
        self.descriptionlabel_6.setText(_translate("PriorityBtn", descriptions_list[5]))

        self.TaskLabel_7.setText(_translate("PriorityBtn", names_list[6]))
        self.datelabel_7.setText(_translate("PriorityBtn", dates_list[6]))
        self.timelabel_7.setText(_translate("PriorityBtn", times_list[6]))
        self.descriptionlabel_7.setText(_translate("PriorityBtn", descriptions_list[6]))

        self.SortBy.setText(_translate("PriorityBtn", "Sort by             Date"))
        self.GroupBy.setText(_translate("PriorityBtn", "Group by     Priority"))

    def open_create_task_window(self):
        self.create_task_window = QtWidgets.QMainWindow()
        create_task_ui = CreateTaskWindow()
        create_task_ui.setupUi(self.create_task_window)
        self.create_task_window.show()

    def open_edit_task_window(self, index):
        self.edit_task_window = QtWidgets.QMainWindow()
        edit_task_ui = EditTaskWindow()
        edit_task_ui.setupUi(self.edit_task_window, index)
        self.edit_task_window.show()




#create new task window
class CreateTaskWindow(object):
    def setupUi(self, CreateTaskWindow):
        CreateTaskWindow.setObjectName("CreateTaskWindow")
        CreateTaskWindow.resize(400, 360)

        #main window
        self.RoundRectangle = QtWidgets.QFrame(parent=CreateTaskWindow)
        self.RoundRectangle.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.RoundRectangle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.RoundRectangle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.RoundRectangle.setStyleSheet("background-color: #dddddd;")
        self.RoundRectangle.setObjectName("RoundRectangle")

        #descriptiton label
        self.DescrptionLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.DescrptionLabel.setGeometry(QtCore.QRect(10, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DescrptionLabel.setFont(font)
        self.DescrptionLabel.setObjectName("DescrptionLabel")

        #description edit
        self.DescriptionEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.DescriptionEdit.setGeometry(QtCore.QRect(180, 60, 171, 31))
        self.DescriptionEdit.setStyleSheet("background-color: #FFFFFF;")
        self.DescriptionEdit.setObjectName("DescriptionEdit")

        #date label
        self.DateLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.DateLabel.setGeometry(QtCore.QRect(10, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")

        #date edit
        self.DateEdit = QtWidgets.QDateEdit(parent=self.RoundRectangle)
        self.DateEdit.setGeometry(QtCore.QRect(180, 110, 171, 31))
        self.DateEdit.setStyleSheet("background-color: #FFFFFF;")
        self.DateEdit.setObjectName("DateEdit")

        #time edit
        self.TimeEdit = QtWidgets.QTimeEdit(parent=self.RoundRectangle)
        self.TimeEdit.setGeometry(QtCore.QRect(180, 150, 171, 31))
        self.TimeEdit.setStyleSheet("background-color: #FFFFFF;")
        self.TimeEdit.setObjectName("TimeEdit")

        #time label
        self.TimeLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.TimeLabel.setGeometry(QtCore.QRect(10, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")

        #interval label
        self.IntervalLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.IntervalLabel.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IntervalLabel.setFont(font)
        self.IntervalLabel.setObjectName("IntervalLabel")

        #interval edit
        self.IntervalEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.IntervalEdit.setGeometry(QtCore.QRect(180, 190, 171, 31))
        self.IntervalEdit.setStyleSheet("background-color: #FFFFFF;")
        self.IntervalEdit.setObjectName("IntervalEdit")

        #priority label
        self.PriorityLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.PriorityLabel.setGeometry(QtCore.QRect(10, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PriorityLabel.setFont(font)
        self.PriorityLabel.setObjectName("PriorityLabel")

        #priority edit
        self.PriorityEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.PriorityEdit.setGeometry(QtCore.QRect(180, 230, 171, 31))
        self.PriorityEdit.setStyleSheet("background-color: #FFFFFF;")
        self.PriorityEdit.setObjectName("PriorityEdit")

        #task label
        self.TaskLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.TaskLabel.setGeometry(QtCore.QRect(10, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TaskLabel.setFont(font)
        self.TaskLabel.setObjectName("TaskLabel")

        #task edit
        self.TaskEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.TaskEdit.setGeometry(QtCore.QRect(180, 20, 171, 31))
        self.TaskEdit.setStyleSheet("background-color: #FFFFFF;")
        self.TaskEdit.setObjectName("TaskEdit")

        #submit task btn
        self.SubmitTask = QtWidgets.QPushButton(parent=self.RoundRectangle)
        self.SubmitTask.setGeometry(QtCore.QRect(20, 280, 321, 31))
        self.SubmitTask.setStyleSheet("background-color: #f6be5d;")
        self.SubmitTask.setObjectName("SubmitTask")
        self.SubmitTask.clicked.connect(lambda: ToDoList().valid_input(self.TaskEdit, self.DescriptionEdit, self.DateEdit,
                                                                       self.TimeEdit, self.IntervalEdit, self.PriorityEdit))

        

        self.retranslateUi(CreateTaskWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateTaskWindow)





    def retranslateUi(self, CreateTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateTaskWindow.setWindowTitle(_translate("CreateTaskWindow", "Create a New Task"))
        self.DescrptionLabel.setText(_translate("CreateTaskWindow", "Description"))
        self.DateLabel.setText(_translate("CreateTaskWindow", "Date"))
        self.TimeLabel.setText(_translate("CreateTaskWindow", "Time"))
        self.IntervalLabel.setText(_translate("CreateTaskWindow", "Interval"))
        self.PriorityLabel.setText(_translate("CreateTaskWindow", "Priority"))
        self.SubmitTask.setText(_translate("CreateTaskWindow", "Create Task"))
        self.TaskLabel.setText(_translate("CreateTaskWindow", "Task Name"))

#edit task window
class EditTaskWindow(object):
    def setupUi(self, CreateTaskWindow, index=None):
        self.index = index

        CreateTaskWindow.setObjectName("CreateTaskWindow")
        CreateTaskWindow.resize(400, 360)

        # main window
        self.RoundRectangle = QtWidgets.QFrame(parent=CreateTaskWindow)
        self.RoundRectangle.setGeometry(QtCore.QRect(20, 20, 361, 331))
        self.RoundRectangle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.RoundRectangle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.RoundRectangle.setStyleSheet("background-color: #dddddd;")
        self.RoundRectangle.setObjectName("RoundRectangle")

        # descriptiton label
        self.DescrptionLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.DescrptionLabel.setGeometry(QtCore.QRect(10, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DescrptionLabel.setFont(font)
        self.DescrptionLabel.setObjectName("DescrptionLabel")

        # description edit
        self.DescriptionEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.DescriptionEdit.setGeometry(QtCore.QRect(180, 60, 171, 31))
        self.DescriptionEdit.setStyleSheet("background-color: #FFFFFF;")
        self.DescriptionEdit.setObjectName("DescriptionEdit")

        # date label
        self.DateLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.DateLabel.setGeometry(QtCore.QRect(10, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")

        # date edit
        self.DateEdit = QtWidgets.QDateEdit(parent=self.RoundRectangle)
        self.DateEdit.setGeometry(QtCore.QRect(180, 110, 171, 31))
        self.DateEdit.setStyleSheet("background-color: #FFFFFF;")
        self.DateEdit.setObjectName("DateEdit")

        # time edit
        self.TimeEdit = QtWidgets.QTimeEdit(parent=self.RoundRectangle)
        self.TimeEdit.setGeometry(QtCore.QRect(180, 150, 171, 31))
        self.TimeEdit.setStyleSheet("background-color: #FFFFFF;")
        self.TimeEdit.setObjectName("TimeEdit")

        # time label
        self.TimeLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.TimeLabel.setGeometry(QtCore.QRect(10, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")

        # interval label
        self.IntervalLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.IntervalLabel.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IntervalLabel.setFont(font)
        self.IntervalLabel.setObjectName("IntervalLabel")

        # interval edit
        self.IntervalEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.IntervalEdit.setGeometry(QtCore.QRect(180, 190, 171, 31))
        self.IntervalEdit.setStyleSheet("background-color: #FFFFFF;")
        self.IntervalEdit.setObjectName("IntervalEdit")

        # priority label
        self.PriorityLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.PriorityLabel.setGeometry(QtCore.QRect(10, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PriorityLabel.setFont(font)
        self.PriorityLabel.setObjectName("PriorityLabel")

        # priority edit
        self.PriorityEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.PriorityEdit.setGeometry(QtCore.QRect(180, 230, 171, 31))
        self.PriorityEdit.setStyleSheet("background-color: #FFFFFF;")
        self.PriorityEdit.setObjectName("PriorityEdit")

        # task label
        self.TaskLabel = QtWidgets.QLabel(parent=self.RoundRectangle)
        self.TaskLabel.setGeometry(QtCore.QRect(10, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TaskLabel.setFont(font)
        self.TaskLabel.setObjectName("TaskLabel")

        # task edit
        self.TaskEdit = QtWidgets.QTextEdit(parent=self.RoundRectangle)
        self.TaskEdit.setGeometry(QtCore.QRect(180, 20, 171, 31))
        self.TaskEdit.setStyleSheet("background-color: #FFFFFF;")
        self.TaskEdit.setObjectName("TaskEdit")

        # submit task btn
        self.SubmitTask = QtWidgets.QPushButton(parent=self.RoundRectangle)
        self.SubmitTask.setGeometry(QtCore.QRect(20, 280, 321, 31))
        self.SubmitTask.setStyleSheet("background-color: #f6be5d;")
        self.SubmitTask.setObjectName("SubmitTask")
        self.SubmitTask.clicked.connect(lambda: ToDoList().edit_task(self.index,self.TaskEdit, self.DescriptionEdit, self.DateEdit,
                                           self.TimeEdit, self.IntervalEdit, self.PriorityEdit))


        self.retranslateUi(CreateTaskWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateTaskWindow)

    def retranslateUi(self, CreateTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateTaskWindow.setWindowTitle(_translate("CreateTaskWindow", "Edit Task"))
        self.DescrptionLabel.setText(_translate("CreateTaskWindow", "Description"))
        self.DateLabel.setText(_translate("CreateTaskWindow", "Date"))
        self.TimeLabel.setText(_translate("CreateTaskWindow", "Time"))
        self.IntervalLabel.setText(_translate("CreateTaskWindow", "Interval"))
        self.PriorityLabel.setText(_translate("CreateTaskWindow", "Priority"))
        self.SubmitTask.setText(_translate("CreateTaskWindow", "Edit Task"))
        self.TaskLabel.setText(_translate("CreateTaskWindow", "Task Name"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PriorityBtn = QtWidgets.QMainWindow()
    ui = ToDoListWindow()
    ui.setupUi(PriorityBtn)
    PriorityBtn.show()
    sys.exit(app.exec())
