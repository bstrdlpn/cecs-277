"""
Long Nguyen, Christina Hipolito
09/26/24

Task List:
Create a program that maintains a task list for the user.  The user should be 
able to view the current task, mark the current task complete, postpone the 
current task, or to add a new task.  The program will read the list from a file 
('tasklist.txt') when the program begins and then store the updated list by 
overwriting the old contents when the user quits the program.
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

    with open('tasklist.txt', 'w') as file:
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
            #should we include something for months with less than 31 days or february?
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
                if int(user_input) < 10 and len(user_input) < 2:
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
                if int(user_input) < 10 and len(user_input) < 2:
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
    """Main loop for planner."""

    # read in contents of file, store in a sorted list
    tasklist = read_file()
    tasklist.sort()

    #repeatedly display the number of tasks and then prompt the user to choose
    while True:
        tasklist.sort()
        print('-Tasklist-')
        num_tasks = len(tasklist)
        if num_tasks == 0:
            print('You have no tasks.')
        elif num_tasks == 1:
            print(f"You have {num_tasks} task.")
        else:
            print(f"you have {num_tasks} tasks.")

        choice = main_menu()

        if choice == 1:
            # display the current task
            if len(tasklist) > 0:
                print('Current task is:')
                print(tasklist[0])
                print()
            else:
                print("Nothing Here! All tasks have been completed.")
                print()
        elif choice == 2:
            # mark the current task as complete
            print('Makring current task as complete:')
            print(tasklist[0])
            del tasklist[0]
            print()
        elif choice == 3:
            # postpone the current task
            print('Postponing task:')
            print(tasklist[0])
            task_name = tasklist[0].get_description()
            new_date = get_date()
            new_time = get_time()
            new_task_object = task.Task(task_name, new_date, new_time)
            tasklist.append(new_task_object)
            del tasklist[0]
            print()
        elif choice == 4:
            # add new task
            desc = str(input("Enter a task: "))
            date = get_date()
            time = get_time()
            new_task = task.Task(desc, date, time)
            tasklist.append(new_task)
            print()
        elif choice == 5:
            # write contents of task list back to file, and exit
            print('Saving and exiting.')
            write_file(tasklist)
            break

main()
