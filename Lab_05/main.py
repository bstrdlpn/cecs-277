"""
Main file (`main.py`) - create the following functions:

"""

import task

def main_menu():
    """
    Display the main menu.
    
    :returns: Int of the user's choice.
    """

    selection = ['1', '2', '3', '4', '5']

    print('1. Display current task')
    print('2. Mark current task complete')
    print('3. Postpone current task')
    print('4. Add new task')
    print('5. Save and quit')
    while True:
        choice = input('Enter choice: ')
        if len(choice) == 1 and choice.isdigit() and choice in selection:
            break
        else:
            print('Invalid input, please select [1-5]')

    return int(choice)


def read_file():
    """
    Open the file (`tasklist.txt`) and read in each of the tasks. 
    
    :returns: Filled list of task objects
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

    # replace testfile.txt with tasklist.txt
    with open('testfile.txt', 'w') as file:
        for object in tasklist:
            file.write(repr(object) + '\n')


def get_date():
    """
    Prompt the user to enter month, day year. 

    :returns: A string in the format MM/DD/YYYY
    """

    month = ''
    day = ''
    year = ''
    is_valid = False

    while not is_valid:
        while True:
            user_input = input('Enter month: ')
            if user_input.isdigit() and 1 <= int(user_input) <= 12:
                    month = user_input
                    break
            else:
                print('Invalid month. Select between [1-12]')
                continue
        while True:
            user_input = input('Enter day: ')
            if user_input.isdigit() and 1 <= int(user_input) <= 31:
                day = user_input
                break
            else:
                print('Invalid day. Select between [1-31]')
                continue
        while True:
            user_input = input('Enter year: ')
            if user_input.isdigit() and 2000 <= int(user_input) <= 2100:
                year = user_input
                is_valid = True
                break
            else:
                print('Invalid year. Select between [2000 - 2100]')
                continue

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
    is_valid = False

    while not is_valid:
        while True:
            user_input = input('Enter hour: ')
            if user_input.isdigit() and 0 <= int(user_input) <= 23:
                if int(user_input) < 10:
                    time_hour = '0' + user_input 
                    break
                else:
                    time_hour = user_input
                    break
            else:
                print('Invalid hour. Select between [0-23]')
                continue
        while True:
            user_input = input('Enter minute: ')
            if user_input.isdigit() and 0 <= int(user_input) <= 59:
                if int(user_input) < 10:
                    time_minute = '0' + user_input    
                    is_valid = True
                    break
                else:
                    time_minute = user_input
                    is_valid = True
                    break
            else: 
                print('Invalid minutes. Select between [0-59]')
                continue
    
    time_string = f"{time_hour}:{time_minute}"

    return time_string

def main():
    # TODO: 
        # read in contents of file, store in sorted list
main()