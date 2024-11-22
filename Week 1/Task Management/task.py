class Task:
    def __init__(self, taskid, taskname, status,priority, location):
        self.taskid = taskid
        self.taskname =taskname
        self.status=status
        self.priority= priority
        self.location= location

    def __str__(self):
        return f"Task Id: {self.taskid}  Task Name: {self.taskname} Status: {self.status} Priority: {self.priority}  Location: {self.location}"