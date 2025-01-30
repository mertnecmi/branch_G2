# tool/task.py
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

bugun = datetime.today()
special_keywords = {
    "bugun" : bugun.strftime('%Y-%m-%d'),
    "yarın" : (bugun+timedelta(days=1)).strftime('%Y-%m-%d'),
    "ghafta" : (bugun+timedelta(weeks=1)).strftime('%Y-%m-%d')
}

class Task(ABC):
    def __init__(self, id, coloru, name,  deadline, priority,  startt=special_keywords["bugun"], status='Pending'):
        self.name = name
        self.deadline = deadline
        self.priority = priority
        self.status = status
        self.coloru = coloru
        self.id = id
        self.startt = startt

    @abstractmethod
    def display_task(self):
        pass

    @abstractmethod
    def mark_as_completed(self):
        pass

    @abstractmethod
    def get_task_type(self):
        pass


class PersonalTask(Task):
    def __init__(self, id, coloru, name, deadline, priority, notes,  startt=special_keywords["bugun"], status='Pending'):
        super().__init__(id, coloru, name,  deadline, priority, startt, status)
        self.notes = notes

    def display_task(self):

        return "{}ID: {:<3} PT: {:<15} Deadline: {:<10} Priority: {:<10} Notes: {:<20} Status: {:<10}".format(
    self.coloru, self.id, self.name[:15], self.deadline, self.priority, self.notes[:20], self.status)


    def mark_as_completed(self):
        self.status = 'Completed'

    def get_task_type(self):
        return 'PersonalTask'


class WorkTask(Task):
    def __init__(self, id, coloru, name, deadline, priority, project_name, startt=special_keywords["bugun"], status='Pending'):
        super().__init__(id, coloru, name, deadline, priority, startt, status)
        self.project_name = project_name
        self.notes =""
    def display_task(self):
        #return f"{self.coloru}ID: {self.id} Work Task: {self.name}, Deadline: {self.deadline}, Priority: {self.priority}, Project: {self.project_name}, Status: {self.status} " 
        return "{}ID: {:<3} WT: {:<15} Deadline: {:<10} Priority: {:<10} Notes: {:<20} Status: {:<10}".format(
    self.coloru, self.id, self.name[:15], self.deadline, self.priority, self.project_name[:20], self.status)
    
    def mark_as_completed(self):
        self.status = 'Completed'

    def get_task_type(self):
        return 'WorkTask'
