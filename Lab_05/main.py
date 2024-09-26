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
    Writes the list of tasks to text file using Task repr() method.

    :param tasklist: list, list of tasks to be written to .txt file.
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
    Prompt the user to enter the hour (military time) and minute.

    :returns: Date in format HH:MM
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
    # read in contents of file, store in a sorted list HINT: try using .sort()
    tasklist = read_file()

    #repeatedly display the number of tasks and then prompt the user to choose
    while True:
        print('-Tasklist-')
        num_tasks = len(tasklist)
        print(f"You have {num_tasks}")
        choice = main_menu():
        match choice:
            case 1:
                # 1. display current task
                    # display first task at index[0]
                    # if no tasks, display a message that says all their tasks are complete 
                pass
            case 2:
                # 2. mark current task complete
                    # display the current task at index[0], remove it and display the 
                    # new current task. if no tasks, display a message
                pass
            case 3:
                # 3. postpone current task
                    # display the current task and prompt the user to enter a new date
                    # and time. 
                        # remove the task from the list
                        # construct a new task using old description with new date, time
                        # add back to list and re-sort
                    # if there are no tasks, display a message
                pass
            case 4:
                # 4. add new task
                    # prompt user to enter a new task desc, date, time
                    # construct task and add to the list, re-sort it
                pass
            case 5:
                # write contents of task list back to file, and exit
                print('Saving and exiting.')
                write_file(tasklist)
                break


    pass
main()