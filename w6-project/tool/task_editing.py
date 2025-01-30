# tool/task_editing.py
from tool.task import *
from tool.task_management import *

class TaskEditing:
    @staticmethod
    def edit_task_priority(task: Task, new_priority: str):
        task.priority = new_priority
        if task.priority == "High":
            task.coloru= "\033[91m"
        print(f"Priority for {task.name} changed to {new_priority}")
       

    @staticmethod
    def edit_task_status(task: Task, new_status: str):
        task.status = new_status
        if task.status == "Completed":
            task.coloru ="\033[90m"
        print(f"Status for {task.name} changed to {new_status}")

    @staticmethod
    def edit_task_deleted(task: Task):
        task.status ="DELETED"
        task.coloru ="\033[9m"
        print(f"Status for {task.name} changed to 'DELETED'")

    @staticmethod
    def edit_task_notes(task: Task, new_note):

        task.notes +="-"+special_keywords["bugun"]
        task.notes +=":"
        task.notes +=new_note

        print(f"Status for {task.name} changed to 'NOTES'")
