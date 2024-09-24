"""
Main file (`main.py`) - create the following functions:

"""

import task

def main_menu():
    """
    displays the main menu and returns the user's valid input
    """
    print('-Tasklist-')
    print(f"")

    pass

def read_file():
    """
    Open the file (`tasklist.txt`) and read in each of the tasks. Each line 
    consists of the task description, due date, and time separated by commas. 
    Construct a task object from each line and add it to a list. 
    Return the filled task list.
    """
    task_list = []

    with open("tasklist.txt", 'r') as file:
        for row in file:
            desc, date, time = row.strip().split(",")
            new_task = task.Task(desc, date, time)
        task_list.append(new_task)

    return task_list


def write_file(tasklist):
    """
    passes in the list of tasks that will be written to the file (`tasklist.txt`). 
    Iterate through the list of tasks and write each one to the file using the 
    Task's repr() method (ie. description, date, and time separated by commas).
    """

    with open(write_file, 'w') as file:
        for object in tasklist:
            #TODO
            # add stuff to iterate through object list
            # enter object and write to file

    pass


def get_date():
    """
    prompts the user to enter the month, day, and year. Valid years are 2000-
    2100, valid months are 1-12, and valid days are 1-31 (no need to verify that it is a correct
    day for the month (ie. Feb 31 st is valid)). Return the date in the format: MM/DD/YYYY.
    If the inputted month or day is less than 10, then add a leading 0 to format it correctly.
    """
    month = ''
    day = ''
    year = ''
    while True:
        month = int(input('Enter month: '))
        if not month.isdigit():
            print('Invalid month.')
        if month < 10:
            month = '0' + str(month)
        else:
            continue
        day = int(input('Enter day: '))
        year = int(input('Enter a year: '))
        if year >= 2000 and year <= 2100:
            break
        else:
            print('Invalid year.')

    due_date = f"{month}/{day}/{year}"

    return due_date


def get_time():
    """
    prompts the user to enter the hour (military time) and minute. Valid hours 
    are 0-23 and valid minutes are 0-59. Return the date in the format: HH:MM. 
    If the inputted hour or minute is less than 10, then add a leading 0 to 
    format it correctly.
    """
    time_hour = ''
    time_minute = ''
    
    while True:
        time_hour = input('Enter hour: ')
        if not time_hour.isdigit():
            print('Invalid time.')
        if 0 <= time_hour <= 23:
            continue
        time_minute = input('Enter minute: ')
        if not time_minute.isdigit():
            print('Invalid time.')
        if time_minute < 10:
            time_minute = '0' + str(time_minute)
            break
    
    time_string = f"{time_hour}:{time_minute}"

    return time_string

def main():
    # TODO: 
        # read in contents of file, store in sorted list
main()