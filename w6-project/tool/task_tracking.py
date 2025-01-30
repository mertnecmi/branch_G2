# tool/task_tracking.py
from tool.task import *

class TaskTracking:
    @staticmethod
    def get_task_status(task: Task):
        return f"{task.coloru}Task Type : {task.get_task_type()} \nTask ID : {task.id} - {task.name} \nStatus : {task.status} \nDeadline : {task.deadline} \nPriority : {task.priority} \nNotes : {task.notes if isinstance(task, PersonalTask) else "None"}\033[0m"

    @staticmethod
    def edit_task_notes(task: Task, new_note: str):
        if not task.notes:
            task.notes = ""  # Ensure task.notes is initialized
        
        task.notes += f" - {special_keywords['bugun']} : {new_note}"
        print(f"Notes for {task.name} updated.")
