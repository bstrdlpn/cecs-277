import tasklist
import check_input
#import tasklist

def main_menu():
    """
    Display the main menu and return the user's valid input.

    :returns: str; user's valid input
    """
    # i don't think this is needed since we are validating with check_input
    # selection = ['1', '2', '3', '4', '5', '6', '7']

    print('1. Display all tasks')
    print('2. Display current task')
    print('3. Add new task')
    print('4. Mark current task complete')
    print('5. Postpone current task')
    print('6. Search tasks by date')
    print('7. Save and quit')


    """while True:
        choice = input('Enter choice: ')
        if len(choice) == 1 and choice.isdigit() and choice in selection:
            break
        else:
            print('Invalid input, please select [1-7]')"""
    
    choice = check_input.get_int_range("Enter choice: ", 1, 7)

    return int(choice)

def get_date():
    """
    Prompt the user to enter the month, day, year. 

    **Constraints**
    :valid months:  1-12
    :valid days: 1-31
    :valid years: 2000-2100
    if input date < 10, add leading 0 to format correctly

    :return: str; date in format MM/DD/YYYY
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
    Prompt user to enter hour, minute in military format.


    **Constraints**
    :valid hours: 0-23
    :valid minutes: 0-59
    inf input hour or minute < 10, add leading 0 to format correctly

    :returns: str; date in format HH:MM
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

# don't think we will need this, tasklist.py handles it
# def read_file():
#     """
#     Open the file (`tasklist-1.txt`) and read in each of the tasks. 
    
#     :returns: Filled list of task objects
#     """
#     task_list = []

#     with open("tasklist-1.txt", 'r') as file:
#         for row in file:
#             desc, date, time = row.strip().split(",")
#             new_task = task.Task(desc, date, time)
#             task_list.append(new_task)

#     return task_list

# don't think we will need this, tasklist.py handles it
# def write_file(tasklist):
#     """
#     Writes the list of tasks to text file using Task repr() method.

#     :param tasklist: list, list of tasks to be written to .txt file.
#     """

#     with open('tasklist-1.txt', 'w') as file:
#         for object in tasklist:
#             file.write(repr(object) + '\n')

def main():
    """
    Construct a Tasklist object and then repeatedly display the number of tasks and then prompt the
    user to choose from the following options until they quit the program:
        1. Display all tasks - displays a numbered list of all the tasks in sorted order. It should be
        using the iterator that you created in the Tasklist class. If there are no tasks to display,
        then display a message.
        2. Display current task - displays the first task using Tasklist's get_current_task method. If
        there are no tasks, then display a message that says all their tasks are complete.
        3. Add new task - Prompts the user to enter a new task description, due date, and time, and
        adds the new task to the list by calling the Tasklist's add_task method.
        4. Mark current task complete - Displays the current task, removes it, and then displays the
        new current task by calling Tasklist's mark_complete method. If there are no tasks, then
        display a message.
        5. Postpone - Displays the current task and then prompts the user to enter a new date and
        time to update the task. If there are no tasks to postpone, then display a message.
        6. Search by date - Prompts the user to enter a date (MM/DD/YYYY). Use the iterator to
        loop through the list, if the task's date is the same as the user's, then display the task
        description. Display an enumerated list of all matching tasks (not just the first one). If
        there are no tasks, then display a message
        7. Save and quit - saves the updated contents of the list back to the file (does not append)
        and then quits the program.
    """
    # create task object
    tasks = tasklist.Tasklist()
    

    #repeatedly display the number of tasks and then prompt the user to choose
    while True:
        print('-Tasklist-')
        num_tasks = len(tasks)
        if num_tasks == 0:
            print('You have no tasks.')
        elif num_tasks == 1:
            print(f"You have {num_tasks} task.")
        else:
            print(f"you have {num_tasks} tasks.")

        choice = main_menu()

        match choice:
            case 1:
                # Display all tasks
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
            case 2:
                # Display current task
                print(tasks.get_current_task())
            case 3:
                # Add new task
                pass
            case 4:
                # Mark current task complete
                pass
            case 5:
                # Postpone current task
                pass
            case 6:
                # Search tasks by date
                pass
            case 7:
                # Save and quit
                pass

        # if choice == 1:
        #     # display all tasks, sorted and numbered
        #     if len(tasklist) > 0:
        #         for i in tasklist:
        #             print(f"{i}. {tasklist[i]}") # use iterator instead
        #     else:
        #         print("Nothing here! All tasks have been completed")
        # elif choice == 2:
        #     # display the current task
        #     if len(tasklist) > 0:
        #         print('Current task is:')
        #         print(tasklist[0])
        #         print()
        #     else:
        #         print("Nothing Here! All tasks have been completed.")
        #         print()
        # elif choice == 3:
        #     # add new task
        #     desc = str(input("Enter a task: "))
        #     date = get_date()
        #     time = get_time()
        #     new_task = task.Task(desc, date, time)
        #     tasklist.append(new_task)
        #     print()
        # elif choice == 4:
        #     # mark the current task as complete
        #     print('Marking current task as complete:')
        #     print(tasklist[0])
        #     del tasklist[0]
        #     print()
        # elif choice == 5:
        #     # postpone the current task
        #     print('Postponing task:')
        #     print(tasklist[0])
        #     task_name = tasklist[0].get_description()
        #     new_date = get_date()
        #     new_time = get_time()
        #     new_task_object = task.Task(task_name, new_date, new_time)
        #     tasklist.append(new_task_object)
        #     del tasklist[0]
        #     print()
        # elif choice == 6:
        #     # search tasks by date
        #     print('Looking for your task:')
        #     search = get_date()
        #     count = 0

        #     # use iterator
        #     for i in tasklist:
        #         if i[1] == search:
        #             print(i)
        #     if count == 0:
        #         print("No tasks due on this date.")
        # else:
        #     # write contents of task list back to file, and exit
        #     print('Saving and exiting.')
        #     write_file(tasklist)
        #     break
main()