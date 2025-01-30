# menu.py
from tool.task_management import TaskManagement
from tool.task_scheduling import TaskScheduling
from tool.task_editing import TaskEditing
from tool.task_tracking import TaskTracking
from tool.task import *
from tool.menu import *


def main():
    task_management = TaskManagement()
    task_scheduling = TaskScheduling()
    task_editing = TaskEditing()
    task_tracking = TaskTracking()

    while True:
        main_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            task_type = input("Enter task type (personal/work): ").strip().lower()
            name = input("Enter task name: ")
            while True:
                try:
                    print("Bugün için 0, Yarın için 1, Gelecek Hafta için 2 veya (YYYY-MM-DD) formatında giriniz")
                    deadline = input("Enter task deadline              : ")
                    if deadline =="0":
                        deadline = special_keywords["bugun"]
                    elif deadline == "1":
                        deadline = special_keywords["yarın"]
                    elif deadline == "2":
                        deadline = special_keywords["ghafta"]
                    else:
                        try:
                            entered_date = datetime.strptime(deadline, '%Y-%m-%d')
                            if entered_date <= bugun:
                                print("Entered date must be greater than today's date.")
                                deadline = None
                            else:
                                deadline = entered_date.strftime('%Y-%m-%d')
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            deadline = None

                except Exception as e:
                    print(e) 
                if not deadline:
                    continue
                else:
                    break
            while True:
                try:
                    priority = input("Enter task priority (High/Medium/Low): ")
                    priority = priority.capitalize()
                    
                    if priority in ("High", "Medium", "Low"):
                        break
                except Exception as e:
                    print("Low, Medium veya High Giriniz",e)
                    continue
            id = len(task_management.task_list) +1
            if task_type == 'personal' or task_type=="Personal":
                notes = input("Enter task notes: ")
                coloru = "\033[93m"
                task = task_scheduling.create_personal_task(id, coloru, name, deadline, priority, notes)
            elif task_type == 'work' or task_type=="Work":
                coloru = "\033[96m"
                project_name = input("Enter project name: ")
                task = task_scheduling.create_work_task(id, coloru, name, deadline, priority, project_name)
            task_management.add_task(task)
            print(f"Task '{task.name}' added successfully!")

        elif choice == '2':
            while True:
                list_alt_menu()
               
                listc = input("Select sorting type :")
                if listc == "1":
                    siralama = "deadline"
                elif listc == "2":
                    siralama = "priority"
                elif listc == "3":
                    siralama = "status"
                elif listc == "4":
                    siralama = "name"
                elif listc == "5":
                    siralama = "ontimeunf"
                elif listc == "6":
                    siralama = "allpending"
                elif listc == "0":
                    break
                else:
                    siralama = "startt"
                 
                task_management.display_tasks(siralama)
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to edit: "))
                task = next((t for t in task_management.task_list if t.id == task_id), None)
                if task:
                    print(task_tracking.get_task_status(task))
                    new_priority = input("Enter new priority (High/Medium/Low): ")
                    if new_priority:
                        task_editing.edit_task_priority(task, new_priority)
                        task_management.save_tasks()
                    new_status = input("Enter new Status (Completed): ")
                    if new_status:
                        task_editing.edit_task_status(task, new_status)
                        task_management.save_tasks()
                else:
                    print("Task not found!")
            except ValueError as e:
                print(e)

        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to Deleted: "))
                task = next((t for t in task_management.task_list if t.id == task_id), None)
                if task:
                    print(task_tracking.get_task_status(task))
                    deletedyn = input("Are you sure you want to delete this task? (y/n) : ")
                    if deletedyn.lower() == "y":
                        task_editing.edit_task_deleted(task)
                        task_management.save_tasks()
                else:
                    print("Task not found!")
            except ValueError as e:
                print(e)

        elif choice == '5':
            print("henüz yapılmadı")

        elif choice == '0':
            break

if __name__ == "__main__":
    main()
