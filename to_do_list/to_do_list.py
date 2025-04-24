import json
list_file = "Ahmed/to_do_list/list.json"


try:
    with open(list_file, "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []


print("Welcome to My To-Do List!")


def add():
    task = input("\nEnter the task name (or type 'Q' to exit): ")
    if task.lower() != "q":
        tasks.append(task)
        with open(list_file, "w") as file:
            json.dump(tasks,file,indent=4)
        

def view():
    
    if len(tasks) == 0:
        print("\nNo tasks yet.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def delete():
    
    view()
    try:
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Removed: {removed}")
            with open(list_file, "w") as file:
                json.dump(tasks,file,indent=4)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n**************")
    try:
        choice = int(input("What do you want to do? (1. Add | 2. View | 3. Remove | 4. Quit): "))
        
        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            delete()
        elif choice == 4:
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    
    except ValueError:
        print("Please enter a number.")
