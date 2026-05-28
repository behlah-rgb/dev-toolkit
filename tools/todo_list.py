tasks = []
while True:
    choice = int(input('''\nMenu:
    1]View Tasks
    2]Add Tasks
    3]Delete Tasks
    4]Terminate
    \n'''))
    if choice == 1:
        if not tasks:  # implicit boolean check
            print('\nNo Task added yet.\n')
        else:
            print('\nTasks:\n')
            for x in tasks:
                print(x)
    elif choice == 2:
        task = input("\nAdd a Task.\n")
        tasks.append(task)
        print("\nYour Tasks:\n")
        for x in tasks:
            print(x)
    elif choice==3:
        delete_task = int(input("\nEnter Task number to be deleted.\n"))
        if delete_task <= len(tasks):
            del tasks[delete_task - 1]
        else:
            print("Invalid Task number.\n")
    elif choice == 4:
        break;
    else:
        print('\nInvalid choice, Try again!\n')
