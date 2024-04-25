class DB:
    def __init__(self):
        self.list_of_dicts = []

def main():
    database = DB()
    while (True):
        command = input("Please enter command: ")
        if command == "ADD":
            add(database)
        elif command == "UPDATE":
            update(database)
        elif command == "LIST":
            display(database)
        elif command == "DETAILS":
            details()
        elif command == "REMOVE":
          remove(database)
        elif command == "EXIT":
            break 
        else:
            print("Ensure input is in correct format: ADD, UPDATE, LIST, DETAILS, REMOVE, EXIT")
    return 0

def display(db_instance):
  if len(db_instance.list_of_dicts) != 0:
      print ("\n___List of all records___")
      for task_dict in db_instance.list_of_dicts:
          for key, value in task_dict.items():
              print("Task: " + key + "\nDescription: " + value)
      print("\n")
  else:
      print("No tasks in database")

def remove(db_instance):
  name = input("Please enter task name: ")
  if len(db_instance.list_of_dicts) != 0 and search(name, db_instance):
    for task_dict in db_instance.list_of_dicts[:]:
      if task_dict.get(name):
          db_instance.list_of_dicts.remove(task_dict)
          print("Task removed")
          return
  print("Error: Task not found or list is empty")


def details():
    print("ADD: add a new task to the list if the name doesn't already exist\nUPDATE: Update the task's description if it exists")
    print("LIST: display current tasks\nREMOVE: remove a task from database\nEXIT: end program")

def add(db_instance):
    while True:
        name = input("Please enter task name: ").upper()
        if search(name, db_instance) is True:
            print("Error: Task already exits. Input new task")
            continue
        break 
        
    desc = input("Please enter task description: ")
    db_instance.list_of_dicts.append({name:desc})

def update(db_instance):
    name = input("Please enter name: ")
    if search(name, db_instance) == True:
        desc = input("Please enter task description: ")
        setNew(name, desc, db_instance)
    else:
        print("Task does not exist: no task to update")

def setNew(name, desc, db_instance):
  for task_dict in db_instance.list_of_dicts:
      if name in task_dict:
          task_dict[name] = desc
          break


def search(name, db_instance):
  if len(db_instance.list_of_dicts) == 0:
    return False
  for task_dict in db_instance.list_of_dicts:
    if name in task_dict:
      return True
  return False


main()