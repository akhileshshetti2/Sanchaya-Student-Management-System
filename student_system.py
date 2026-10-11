import csv
import os

class Student:
    """A blueprint representing an individual student record."""

    def __init__(self, student_id, name, age, marks):
        # Initialize the student's core attributes
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display_student(self):
        """Prints a formatted string of the student's details."""
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Marks: {self.marks}")

    def to_dict(self):
        """Converts the student object into a dictionary for easy CSV saving later."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }
        



class StudentManagementSystem:
    """A manager class to handle a collection of students, file operations, and system logic."""

    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_from_csv()  # Automatically load existing data when the system starts

    def add_student(self, student_id, name, age, marks):
        """Creates a new student and adds them to the system list."""
        # Check if student ID already exists
        for student in self.students:
            if student.student_id == student_id:
                print(f"Error: Student with ID {student_id} already exists!")
                return
        
        new_student = Student(student_id, name, age, marks)
        self.students.append(new_student)
        self.save_to_csv()
        print(f"Success: Student {name} added successfully!")

    def view_students(self):
        """Displays all students currently registered in the system."""
        if not self.students:
            print("No student records found.")
            return
        
        print("\n--- Student Records ---")
        for student in self.students:
            student.display_student()
        print("-" * 25)

    def search_student(self, student_id):
        """Searches for a student by their unique ID."""
        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found:")
                student.display_student()
                return student
        print(f"Error: Student with ID {student_id} not found.")
        return None

    def delete_student(self, student_id):
        """Deletes a student record based on their unique ID."""
        student_to_delete = self.search_student(student_id)
        if student_to_delete:
            self.students.remove(student_to_delete)
            self.save_to_csv()
            print(f"Success: Student ID {student_id} deleted successfully!")

    def save_to_csv(self):
        """Saves all current student records to a CSV file."""
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["student_id", "name", "age", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for student in self.students:
                writer.writerow(student.to_dict())

    def load_from_csv(self):
        """Loads student records from the CSV file into memory if it exists."""
        if not os.path.exists(self.filename):
            return  # File doesn't exist yet, which is fine for the first run
        
        with open(self.filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.students = []  # Reset list before loading
            for row in reader:
                # CSV reads everything as strings, so convert age and marks back to correct types
                student = Student(
                    student_id=row["student_id"],
                    name=row["name"],
                    age=int(row["age"]),
                    marks=float(row["marks"])
                )
                self.students.append(student)
                
                
                

def main():
    """The main entry point and user interface loop for the application."""
    system = StudentManagementSystem()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            try:
                age = int(input("Enter Age: ").strip())
                marks = float(input("Enter Marks: ").strip())
                system.add_student(s_id, name, age, marks)
            except ValueError:
                print("Error: Age must be an integer and marks must be a number!")

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            s_id = input("Enter Student ID to search: ").strip()
            system.search_student(s_id)

        elif choice == "4":
            s_id = input("Enter Student ID to delete: ").strip()
            system.delete_student(s_id)

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()