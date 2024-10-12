tasks = []

def add_task(name, description, status=False):
    new_task = {'name': name, 'description': description, 'status': status}
    tasks.append(new_task)
    print(f"{name} was added to the task manager")

def delete_task(name):
    for task in tasks:
        if name in task['name']:
            confirm = input(f"{name} will be deleted, please type 'yes' to delete").lower()
            if confirm == "yes":
                tasks.remove(task)
                print(f"{name} was permanently deleted")
            else:
                print("Nothing was deleted. Returning back to main menu")

def complete_task(name):
    for task in tasks:
        if name in task['name']:
            task['status'] = True
            print(f"{name} has been marked as complete")

while True:
    start = input("What would you like to do? - Type 'View', 'Add', 'Delete', 'Complete'\n").lower()

    if start == 'view':
        if len(tasks) > 0:
            for task in tasks:
                print(f"{task['name']}: {task['description']}, Completed: {task['status']}")
        else:
            print("Sorry there are no tasks in the project manager yet")
    elif start == 'add':
        name = input("What would you like to name the project?").title()
        description = input("What is the description of the task?")
        add_task(name, description)
    elif start == 'delete':
        print('Warning this will permanently delete a task')
        name = input('Please enter the project name you wish to delete.').title()
        delete_task(name)
    elif start == 'complete':
        name = input("Which task would you like to mark as complete?").title()
        complete_task(name)
    else:
