"""
Attributes:
1. description - string description of the task.
2. date - due date of the task. A string in the format: MM/DD/YYYY 
3. time - time the task is due. A string in the format: HH:MM

Methods:
1. __init__(self, desc, date, time) - assigns the parameters to the attributes.
2. get_description(self) - returns the task's description string.
3. __str__(self) - returns a string used to display the task's information to 
    the user in the format: description - Due: date at time.
4. __repr__(self) - returns a string used to write the task's information to the 
    file in the format: task,date,time.
5. __lt__(self, other) - returns true if the self task is less than the other 
    task. Compare by year, then month, then day, then hour, then minute, and 
    then the task description in alphabetical order.
"""

class Task:
    """
    Attributes:
     :description:  string, description of the task
     :date:         string, due date of the task MM/DD/YYYY
     :time:         string HH:MM

     Methods:
     __init__(self, desc, date, time):  assigns the params to the attributes
     get_description(self) :            returns the task's description string
     __str__(self):                     returns a string used to display the 
                                        task's information to the user in the 
                                        format:
    __repr__(self): returns a string used to write the task's information to the file in the format
    __lt__(self, other): returns true if the self task is less than the other task
    """