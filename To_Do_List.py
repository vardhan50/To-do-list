# Function to display the to-do list
def display_tasks(tasks):
    if len(tasks) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("\nEnter a task: ")
    tasks.append(task)

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("\nTask removed successfully!")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nPlease enter a valid number.")

# Function to clear the to-do list
def clear_all(tasks):
    tasks.clear()
    print("\nAll tasks have been cleared.")

# Main program
def main():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            clear_all(tasks)
        elif choice == "5":
            print("\nExiting To-Do List program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
