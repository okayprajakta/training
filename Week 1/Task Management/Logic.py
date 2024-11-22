from task import Task
class logic:
    def __init__(self):
        self.tasks=[]
       
    def add(self, task_to_be_added):
        for i in self.tasks:
            if i.taskid== task_to_be_added.taskid:
                return False
        self.tasks.append(task_to_be_added)
        return True
    
    def update(self, task):
        for t in self.tasks:
            if task.taskid==task.taskid:
                t.status=task.status
                t.priority=task.priority
                t.location=task.location
                return True
        return False

    def delete(self, task):
        for t in self.tasks:
            if t.taskid == task.taskid:
                self.tasks.remove(t)
                return True
        return False
    
    # Function to sort tasks by task name
    def sort_tasks_by_name(self):
        return sorted(self.tasks, key=lambda task: task.task_name)

    # Function to sort tasks by priority
    def sort_tasks_by_priority(self):
        return sorted(self.tasks, key=lambda task: task.priority)

    # Function to sort tasks by location
    def sort_tasks_by_location(self):
        return sorted(self.tasks, key=lambda task: task.location)

    # Function to filter tasks by location
    def filter_tasks_by_location(self, location):
        return list(filter(lambda task: task.location == location, self.tasks))
    


    def view_all(self):
        return self.tasks
    
