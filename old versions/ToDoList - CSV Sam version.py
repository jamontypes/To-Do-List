import csv
import os
import tkinter as tk

def create_file():
    if os.path.isfile("database.csv"):
        # VALIDES FILE IS MADE - IF FILE ISNT THERE FIRST RUN SHOULD BE BLANK
        # IF THE FILE DOES EXIST, IT SHOULD PRINT:
        #[['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Intervals']]
        # with open('database.csv') as csv_file:
        #     csv_reader = csv.reader(csv_file,delimiter=',')
        #     cols = []
        #     for row in csv_reader:
        #         cols.append(row)
        #         break
        # print(cols)
        pass
    else:
        with open('database.csv', 'w', newline='') as csvfile:
            fieldnames = ['task_id', 'Names','Descriptions','Dates','Times','Interval']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

def get_last_task_id():
    if os.path.isfile("database.csv"):
        with open('database.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            tasks = list(reader)
            if tasks:
                last_task = tasks[-1]
                return int(last_task['task_id'])
    return 0

def new_task():
    repeat_intervals = ["never", "hourly", "daily", "weekly"]
    name = input("Enter Name:")
    info = input("Enter Description:")

    date = input("Enter Date (MM/DD/YY):")
    while date[2] != "/" or date[5] != "/":
        print("Invalid format")
        date = input("Enter Date (MM/DD/YY):")

    valid_times = ["AM","PM"]
    time = input("Enter Time (HH:MM AM/PM):")
    while time[2] != ":" or time[6:8] not in valid_times:
        print("\nInvalid format")
        time = input("Enter Time (HH:MM AM/PM):")

    print("Valid Intervals: 'never', 'hourly', 'daily', 'weekly'")
    repeat = input("Interval:")
    while repeat not in repeat_intervals:
        print("Enter a vaild interval")
        repeat = input("Interval:")

    write2file(name,info,date,time,repeat)
    print(f"\nNew Task:{name} \nDescription: '{info}'")
    print(f'{date}, at {time}')
    print(f"repeats {repeat}")

def write2file(name,description,date,time,interval):
    create_file()
    last_task_id = get_last_task_id()
    next_task_id = last_task_id + 1

    with open('database.csv', 'a', newline='') as csvfile:
        fieldnames = ['task_id', 'Names', 'Descriptions', 'Dates', 'Times', 'Intervals']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({
            'task_id': next_task_id,
            'Names': name,
            'Descriptions': description,
            'Dates': date,
            'Times': time,
            'Intervals': interval
        })


def menu():
    # text based menu, before the gui is added
    valid_options = ["N", "D", "E", "A"]
    print("Welcome! -----------------------------------------------")
    option = input(f'Options: \n\tCreate New Task: "N" \n\tDelete Task: "D" \n\tEdit Task: "E" \n\tShow All Tasks: "A"')
    while option not in valid_options:
        print("Enter a valid option")
        option = input()
    if option == "N":
        new_task()
        menu()
    elif option == "D":
        del_id = input(f'Which task do you want to delete?\nEnter task number:')
        print(del_id)
    elif option == "E":
        print('in prog - edit task')
        menu()
    elif option == "A":
        print('in prog - show all tasks / change to gui')
        menu()


def main():
    if __name__ == "__main__":
        create_file()

new_task()
