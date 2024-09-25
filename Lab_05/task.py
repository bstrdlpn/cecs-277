class Task:
    """
    A task in a planner with due date and time.

    Attributes
    ----------
    description  :  str
        Description of the task.
    date  :  str
        Due date of the task in the format MM/DD/YYYY 
    time  :  str
        Time the task is due in the format HH:MM

    Methods
    -------
    __init__(self, desc, date, time)
        assigns the parameters to the attributes.
    get_description(self)
        returns the task's description string.
    __str__(self)
        returns a string used to display the task's information to the user in 
        the format: description - Due: date at time.
    __repr__(self)
        returns a string used to write the task's information to the  file in 
        the format: task,date,time.
    __lt__(self, other)
        returns true if the self task is less than the other task. Compare by 
        year, then month, then day, then hour, then minute, and then the task 
        description in alphabetical order.
    """

    def __init__(self, desc, date, time):
        """
        Assign parameters to the task object

        :param desc: Description of the task
        :param date: Due date in format MM/DD/YYYY
        :param time: Due time in format HH:MM
        """

        self.desc = desc
        self.date = date
        self.time = time
    
    
    def get_description(self):
        """Return the task description as a string"""
        return self.desc

    
    def __str__(self):
        """
        Return a string used to display the task information to the user in 
        the format: 
        {desc} - Due: {date} at {time}
        """

        return f"{self.desc} - Due: {self.date} at {self.time}"

    
    def __repr__(self):
        """
        Return string used to write the task information to the file in the 
        format: 
        {task},{date},{time}
        """

        return f"{self.desc},{self.date},{self.time}"


    def __lt__(self, other):
        """
        Return true if the self task is less than the other task. Compares by 
        year, month, day, hour, minute and task description in alpha order.
        """
        
        # break MM/DD/YYYY string into month, day, year
        self_month, self_day, self_year = map(int, self.date.split('/'))

        other_month, other_day, other_year = map(int, other.date.split('/'))
        
        # break HH:MM string into hour, minutes
        self_hour, self_minute = map(int, self.time.split(':'))

        other_hour, other_minute = map(int, other.time.split(':'))
        
        # compare by year
        if self_year != other_year:
            return self_year < other_year        
        # compare by month
        elif self_month != other_month:
            return self_month < other_month
        # compare by day
        elif self_day != other_day:
            return self_month < other_month
        # compare by hours
        elif self_hour != other_hour:
            return self_hour < other_hour
        #compare by minutes
        elif self_minute != other_minute:
            return self_minute < other_minute
        else:
            return self.desc < other.desc