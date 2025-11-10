# Program using Classes and Objects

class Student:
    # Constructor to initialize data
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to display student details
    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")

    # Method to check if student passed or failed
    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass 🎉")
        else:
            print("Result: Fail ❌")


# ---- Main Program ----
print("=== Student Information System ===")

# Take input from user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))

# Create an object (instance) of the Student class
student1 = Student(name, roll_no, marks)

# Call class methods using the object
student1.display_info()
student1.check_result()
