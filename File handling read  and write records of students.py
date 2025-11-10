# Program to write and read student records using file handling

def write_records():
    with open("students.txt", "a") as f:  # 'a' means append mode
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")
        f.write(f"{name},{roll},{marks}\n")
        print("Record added successfully!\n")

def read_records():
    try:
        with open("students.txt", "r") as f:
            print("\n--- Student Records ---")
            for line in f:
                name, roll, marks = line.strip().split(",")
                print(f"Name: {name}, Roll No: {roll}, Marks: {marks}")
    except FileNotFoundError:
        print("\nNo records found! Please add records first.\n")

# Main Menu
while True:
    print("\n1. Add Student Record")
    print("2. View All Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_records()
    elif choice == "2":
        read_records()
    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
