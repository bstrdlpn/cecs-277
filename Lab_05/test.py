import task

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

def main():

    task_list = read_file()
    print(len(task_list))
    
    for item in task_list:
        print(item)
main()