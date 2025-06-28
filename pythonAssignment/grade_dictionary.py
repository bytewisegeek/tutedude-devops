student_grades = {}

def add_student():
    name = input("Enter student name: ")
    if name in student_grades:
        print(f"{name} already exists. Use update option instead.")
    else:
        grade = input("Enter grade for student: ")
        student_grades[name] = grade
        print(f"Added {name} with grade {grade}.")

def update_grade():
    name = input("Enter student name to update: ")
    if name in student_grades:
        grade = input("Enter new grade: ")
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} not found in records.")

def print_all_grades():
    if not student_grades:
        print("No student records available.")
    else:
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

# Menu loop
while True:
    print("\n--- Student Grade System ---")
    print("1. Add Student")
    print("2. Update Student Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        print_all_grades()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")