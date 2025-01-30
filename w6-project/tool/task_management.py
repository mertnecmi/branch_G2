# tool/task_management.py (güncelleme)
import json
from tool.task import Task, PersonalTask, WorkTask, special_keywords
from datetime import datetime, timedelta

class TaskManagement:
    def __init__(self, task_file='data/tasks.json'):
        self.task_list = []
        self.task_file = task_file
        self.load_tasks()

    def add_task(self, task):
        self.task_list.append(task)
        self.save_tasks()

    def display_tasks(self, siralama):
        gecikenler = None
        if siralama == "status":
            self.task_list.sort(key=lambda x: x.status)
        elif siralama == "deadline":
            self.task_list.sort(key=lambda x: x.deadline)
        elif siralama == "priority":
            self.task_list.sort(key=lambda x: x.priority)
        elif siralama == "name":
            self.task_list.sort(key=lambda x: x.name)
        elif siralama == "startt":
            self.task_list.sort(key=lambda x: x.startt)
        elif siralama == "ontimeunf":
            msg = "On Time Unfinished Task"
            gecikenler = [task for task in self.task_list if task.status == "Pending" and task.deadline < special_keywords["bugun"]]
        elif siralama == "allpending":
            msg = "All Pending"
            gecikenler = [task for task in self.task_list if task.status == "Pending" ]
        if not gecikenler: 
            for task in self.task_list:
                print(task.display_task(), end="\033[0m \n")
        else:
            print("-----------------------------------------------------")
            print(msg)
            for task in gecikenler:
                print(task.display_task(), end="\033[0m \n")

    def save_tasks(self):
        with open(self.task_file, 'w', encoding="utf-8") as file:
            json.dump([{
                'id':task.id,
                'coloru':task.coloru,
                'name': task.name,
                'deadline': task.deadline,
                'priority': task.priority,
                'startt': task.startt,
                'status': task.status,
                'project_name': task.project_name if isinstance(task, WorkTask) else "None",
                'notes': task.notes if isinstance(task, PersonalTask) else "None",
                'task_type': task.get_task_type(),  # task_type bilgisini ekliyoruz
            } for task in self.task_list], file, indent=4)

    def load_tasks(self):
        try:
            with open(self.task_file, 'r', encoding="utf-8") as file:
                tasks_data = json.load(file)
                tasks_data = sorted(tasks_data, key=lambda x: x['task_type'])
                for task_data in tasks_data:
                    task_type = task_data.get('task_type')
                    if task_type == 'PersonalTask':
                        task = PersonalTask(
                            id=task_data["id"],
                            coloru=task_data["coloru"],
                            name=task_data['name'],
                            deadline=task_data['deadline'],
                            priority=task_data['priority'],
                            startt=task_data['startt'],
                            status=task_data['status'],  # status bilgisini burada da alıyoruz
                            notes=task_data.get('notes', '')  # notes'ı ekliyoruz
                        )
                    elif task_type == 'WorkTask':
                        task = WorkTask(
                            id=task_data["id"],
                            coloru=task_data["coloru"],
                            name=task_data['name'],
                            startt=task_data['startt'],
                            deadline=task_data['deadline'],
                            priority=task_data['priority'],
                            status=task_data['status'],  # status bilgisini burada da alıyoruz
                            project_name=task_data.get('project_name', '')  # project_name'i ekliyoruz
                        )
                    else:
                        continue
                    self.task_list.append(task)
        except FileNotFoundError:
            self.task_list = []
