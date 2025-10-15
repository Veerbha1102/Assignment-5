# task1_student_marks.py

# 1. Creates a dictionary where student names are keys and their marks are values.
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

# 2. Asks the user to input a student's name.
student_name = input("Enter the name of the student to check their marks: ")

# Standardize input for case-insensitive check (optional but good practice)
# student_name = student_name.strip().title() 

# 3. Retrieves and displays the corresponding marks.
# 4. If the student’s name is not found, display an appropriate message.

# Using .get() is a clean way to handle missing keys
marks = student_marks.get(student_name)

if marks is not None:
    print(f"The marks for {student_name} are: {marks}")
else:
    print(f"Error: Student '{student_name}' was not found in the records.")
