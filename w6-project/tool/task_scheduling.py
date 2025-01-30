# tool/task_scheduling.py
from tool.task import PersonalTask, WorkTask
from datetime import datetime

class TaskScheduling:
    def create_personal_task(self, id,coloru, name, deadline, priority, notes):
        task = PersonalTask(id, coloru, name, deadline, priority, notes)
        return task

    def create_work_task(self, id, coloru, name, deadline, priority, project_name):
        task = WorkTask(id, coloru, name, deadline, priority, project_name)
        return task
