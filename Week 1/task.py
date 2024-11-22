def update_task(list, task_id):
    for i in list:
        if i["Task ID"] == task_id:
            i["Status"]="run"
        break

def delete_task(task_id):
    if check_if_task_exists(task_id):
        print(f"{task_id} does not exist.")

    for i in range(len(tasks)):
        if tasks[i]['Task ID'] == task_id:
            del tasks[i]
            break

def running_task():
    for task in tasks:
        if task["Status"] == "running":
            print(f"Task ID : {task["Task ID"]}, Status : {task["Status"]}")

def check_if_task_exists(task_id):
    for task in tasks:
        if task["Task ID"] == task_id:
            return True
    return False

def display_task(tasks):
    for i in tasks:
        print(f"Task ID:{i["Task ID"]}, Status:{i["Status"]}")

def add_task(Id, status, task) :
    dict={"Task ID": Id, "Status":status}
    task.append(dict)

def start():
    tasks=[]
    add_task(1,"Running", tasks)
    add_task(2,"Stopped", tasks)
    #print(task)
    update_task(tasks, 2)
    display_task(tasks)

start()