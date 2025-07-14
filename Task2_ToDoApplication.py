def task():
    tasks = []
    print("Welcome to Task Management App")

    total_tasks = int(input("Enter number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print("Today's tasks are: {tasks}")
    
    while True:
        opr = int(input("Choose an option\n1: Add\n2: Update\n3: Delete\n4: View\n5: Stop\n"))
        
        if opr == 1:
            add = input("Enter your task to be added: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
        
        elif opr == 2:
            upd_val = input("Enter the task you want to update: ")
            if upd_val in tasks:
                upd = input("Enter your new task: ")
                ind = tasks.index(upd_val)
                tasks[ind] = upd
                print(f"Updated task: {upd}")
            else:
                print("Task not found.")
        
        elif opr == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been successfully deleted.")
            else:
                print("Task not found")
        
        elif opr == 4:
            print(f"Your tasks are: {tasks}")
        
        elif opr == 5:
            print("Closing the program... ")
            break
        
        else:
            print("Invalid input")
task()            