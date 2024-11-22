from Logic import logic
from task import Task

def test_logic_functions():
    # Create an instance of Logic
    task_manager = logic()

    # Create some tasks
    t1 = Task(1, "Task 1", "Running", "High", "COIMBATORE")
    t2 = Task(2, "Task 2", "Running", "Medium", "DELHI")
    t3 = Task(3, "Task 3", "Stopped", "Low", "MUMBAI")
    t4 = Task(4, "Task 4", "Stopped", "High", "THANE")

    # 1. Test Adding Tasks
    ("Adding Tasks:")
    (task_manager.add(t1))  
    (task_manager.add(t2))  
    (task_manager.add(t3))  
    (task_manager.add(t4))  
    (task_manager.add(t1))  

    # 2. Test Viewing All Tasks
    print("\nAll Tasks:")
    for task in task_manager.view_all():
        print(task)

    # 3. Test Updating a Task
    print("\nUpdating Task 1:")
    updated_task = Task(1, "Updated Task 1", "Stopped", "Low", "PUNE")
    print(task_manager.update(updated_task))

    # 4. View All Tasks After Update
    print("\nAll Tasks after update:")
    for task in task_manager.view_all():
        print(task)

    # 5. Test Viewing Tasks by Location
    print("\nTasks in DELHI:")
    for task in task_manager.filter_tasks_by_location("DELHI"):
        print(task)

    # 6. Test Deleting a Task
    print("\nDeleting Task 1:")
    print(task_manager.delete(t1)) 

    # 7. View All Tasks After Deletion
    print("\nAll Tasks after deletion:")
    for task in task_manager.view_all():
        print(task)

if __name__ == "__main__":
    test_logic_functions()