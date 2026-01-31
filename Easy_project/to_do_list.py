Tasks =[]
Done_tasks = []
while True:
    print("\nTo-Do-List")
    print("1.Add task: ")
    print("2.View task")
    print("3.Mark as done")
    print("4.View done tasks")
    print("5.Delete task")
    print("6.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task_name = input("Enter your task: ")
        Tasks.append(task_name)
        print(f"{task_name} has been added.")
    elif choice == "2":
        if not Tasks:
            print("No task yet.")
        else:
            print("Your task")
            for i, task in enumerate(Tasks, 1):
                print(f"{i}.{task}")
    elif choice == "3":
            name = input("Enter name: ")
            if name in Tasks:
                 Done_tasks.append(name)
                 Tasks.remove(name)
                 print(f"{name} marked as done.")
    elif choice == "4":
            if not Done_tasks:
                 print("No tasks yet.")
            else:
                 print("Your tasks are:")
                 for i, task in enumerate (Done_tasks, 1):
                      print(f"{i}.{task}")
    elif choice == "5":
            name_to_delete = input("Enter name to delete: ")
            if name_to_delete in Tasks:
                 Tasks.remove(name_to_delete)
                 print(f"{name_to_delete} has been deleted.")
            else:
                 print(f"{name_to_delete} does not exist.")
    elif choice == "6":
            print("Goodbye!")
            break
    else:
         print("Invalid choice. Please try again.")


