# main.py

from student_management.student import (
    add_student, update_student, delete_student,
    view_students, search_student, generate_report
)

def main():
    students = []
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search for a Student")
        print("6. Generate Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            view_students(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            generate_report(students)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
