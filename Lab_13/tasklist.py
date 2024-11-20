import task

class Tasklist:
    def __init__(self):
        """
        Read in the initial list of tasks from the file 'tasklist.txt', 
        constructs the task object, store in list of tasks. Sort the list.
        """
        self._tasklist = []

        with open ('tasklist-1.txt', 'r') as file:
            for row in file:
                desc, date, time = row.strip().split(",")
                new_task = task.Task(desc, date, time)
                self._tasklist.append(new_task)

        # after we initialize, sort the list
        self._tasklist.sort()

    def add_task(self, desc, date, time):
        """
        Use the parameters to construct a new task object, then store it into 
        the tasklist. Sort the list after the task is added.

        :param desc: str; description of the task
        :param date: str; date of the task in format MM/DD/YYYY
        :param time: str; time of the task in format HH:MM        """
        new_task = task.Task(desc, date, time)
        self._tasklist.append(new_task)
        self._tasklist.sort()
    
    def get_current_task(self):
        """
        Return the first task object.
        """
        return self._tasklist[0]

    def mark_complete(self):
        """
        Remove the first task from the tasklist and return it.
        """
        completed_task = self._tasklist[0]
        del self._tasklist[0]
        return completed_task

    def postpone_task(self, date, time):
        """
        Remove the first task from the tasklist. Use its description, the new date, and the new
        time to construct a new task. Add that task to the tasklist and resort the list.
        """
        task_desc = self._tasklist[0].get_description()
        del self._tasklist[0]
        postpone_task = task.Task(task_desc, date, time)
        self._tasklist.append(postpone_task)
        self._tasklist.sort()

    def save_file(self):
        """
        Write the list of tasks to text file.
        """
        with open('tasklist.txt', 'w') as file:
            for task in self._tasklist:
                file.write(repr(object) + '\n')
    
    def __iter__(self):
        """
        Initialize the _n attr and return self.
        """
        self._n = 0
        return self


    def __len__(self):
        """
        Return the number of Task objets in the tasklist.
        """
        return len(self._tasklist)
    
    
    def __next__(self):
        """
        Iterate the iterator one position at a time. Raise a StopIteration when the iterator reaches
        the end of the tasklist, otherwise return the Task object at the iterator's current position.
        """
        if self._n < len(self._tasklist):
            task = self._tasklist[self._n]
            self._n += 1
            return task
        else:
            raise StopIteration