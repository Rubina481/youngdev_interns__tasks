# -----------------------------------------------
# 📝 To-Do List App using Classes and File Handling
# -----------------------------------------------
# Features:
# 1. Add a new task
# 2. View all tasks
# 3. Delete a task by number
# 4. Exit program
# -----------------------------------------------

class ToDoList:
    """A simple class to manage To-Do tasks stored in a text file."""

    # Constructor to initialize the filename
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    # ---------- Add a new task ----------
    def add_task(self, task):
        """Append a new task to the file."""
        with open(self.filename, "a") as file:
            file.write(task + "\n")  # Add task and move to next line
        print("✅ Task added successfully!")

    # ---------- View all tasks ----------
    def view_tasks(self):
        """Read and display all tasks from the file."""
        try:
            with open(self.filename, "r") as file:
                tasks = [t.strip() for t in file.readlines()]  # Remove newline characters

            if tasks:
                print("\n📋 Your To-Do Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("\n📭 No tasks found!")
        except FileNotFoundError:
            print("\n⚠️ No task file found yet. Please add a task first.")

    # ---------- Delete a task ----------
    def delete_task(self, num):
        """Delete a specific task by its number."""
        try:
            with open(self.filename, "r") as file:
                tasks = file.readlines()

            if 1 <= num <= len(tasks):
                del tasks[num - 1]  # Remove selected task
                with open(self.filename, "w") as file:
                    file.writelines(tasks)  # Rewrite file without deleted task
                print("🗑️ Task deleted successfully!")
            else:
                print("❌ Invalid task number!")
        except FileNotFoundError:
            print("\n⚠️ No tasks to delete.")


# ---------- Main Program ----------
def main():
    """Main function to run the To-Do List app."""
    todo = ToDoList()  # Create object of ToDoList class

    while True:
        # Display the main menu
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Perform actions based on user choice
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                todo.delete_task(num)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# ---------- Run Program ----------
if __name__ == "__main__":
    main()
