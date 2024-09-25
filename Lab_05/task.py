class Task:
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

    def __init__(self, desc, date, time):
        """assign parameters to the attributes"""
        self.desc = desc
        self.date = date
        self.time = time
    
    
    def get_description(self):
        """return task description string"""
        return self.desc
        pass
    
    def __str__(self):
        """returns a string used to display the task’s information to the user in the format:
        'desc' - Due: `date` at `time`"""
        return f"{self.desc} - Due: {self.date} at {self.time}"
        pass
    
    def __repr__(self):
        """returns a string used to write the task’s information to the file in the format: task,date,time"""
        return self.desc + "," + str(self.date) + "," + str(self.time)
        pass
    
    def __lt__(self, other):
        """
        return true if the self task is less than the other task.
        compare by year, then month, then day, then hour, then minute, and then the task description in alphabetical order
        """
        if self.date(year) < other.date(year):
            return True
        elif self.date(year) == other.date(year):
            if self.date(month) < other.date(month):
                return True
            elif self.date(month) == other.date(month):
                if self.date(day) < other.date(day):
                    return True
                elif self.date(day) == other.date(day): 
                    if self.time(hour) < other.time(hour):
                        return True
                    elif self.time(hour) == other.time(hour):
                        if self.time(minute) < other.time(minute):
                            return True
                        else:
                            return False
        else:
            return false
        pass