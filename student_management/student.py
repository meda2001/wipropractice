# student_management/student.py

def add_student(students):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    gpa = float(input("Enter student's GPA: "))
    is_enrolled = input("Is the student enrolled? (yes/no): ").strip().lower() == 'yes'
    student = {
        'name': name,
        'age': age,
        'gpa': gpa,
        'is_enrolled': is_enrolled
    }
    students.append(student)
    print(f"Student {name} added successfully.")

def update_student(students):
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student['name'] == name:
            student['age'] = int(input("Enter new age: "))
            student['gpa'] = float(input("Enter new GPA: "))
            student['is_enrolled'] = input("Is the student enrolled? (yes/no): ").strip().lower() == 'yes'
            print(f"Student {name} updated successfully.")
            return
    print(f"Student {name} not found.")

def delete_student(students):
    name = input("Enter the name of the student to delete: ")
    for i, student in enumerate(students):
        if student['name'] == name:
            del students[i]
            print(f"Student {name} deleted successfully.")
            return
    print(f"Student {name} not found.")

def view_students(students):
    if not students:
        print("No students to display.")
        return
    for student in students:
        print(student)

def search_student(students):
    name = input("Enter the name of the student to search: ")
    for student in students:
        if student['name'] == name:
            print(student)
            return
    print(f"Student {name} not found.")

def generate_report(students):
    if not students:
        print("No students to generate report.")
        return
    total_gpa = sum(student['gpa'] for student in students)
    average_gpa = total_gpa / len(students)
    print(f"Average GPA: {average_gpa:.2f}")
    threshold = float(input("Enter GPA threshold: "))
    print("Students with GPA above threshold:")
    for student in students:
        if student['gpa'] > threshold:
            print(student)
