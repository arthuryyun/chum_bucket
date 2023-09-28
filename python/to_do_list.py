"""
title: to-do list
purpose: to-do list
author: @arthuryyun
"""

def main():
    tasks = []
    while True:
        print("\nTo-Do List") #augment \n to identify the purpose of \n
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ") 

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)

        elif choice == "2":
            print("\nTasks:")
            for index, task in enumerate(tasks,1):
                print(f"{index}. {task}")

        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            if 0 < task_number <= len(tasks):
                del tasks[task_number - 1]
                print("Task deleted!")

            else:
                print("Invalid task number.")
        
        elif choice == "4":
            print("Goodbye!")
            break 

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

