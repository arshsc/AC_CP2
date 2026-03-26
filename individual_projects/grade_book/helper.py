import csv

student_file = "individual_projects/grade_book/docs/students.csv"


class Student:
    def __init__(self, name, student_id, grades=[]):
        self.name = name
        self.student_id = int(student_id)
        self.grades = grades

    def grade_average(self):
        pass

    def display(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}\n"

    @staticmethod
    def to_dict(self):
        return {"radius": self.name, "area": self.student_id, "circumference": self.grades}
    
class GradeBook:
    def __init__(self):
        pass

def load_csv(filename):
    try:
        with open(filename, "r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

students = load_csv(student_file)

def add_new_student():
    print("\n=====================================\n\nADD NEW STUDENT\n\n=====================================")
    student_name = input("\nEnter Student Name: ").title()

    while True:
        student_id = input("Enter Student ID: ")
        if student_id.isdigit() == False:
            print("\nInvalid Input")
        elif student_id.isdigit() == True:
            break
    
    student = Student(student_name, student_id)

    with open(student_file, "a", newline="") as file:
        fieldnames = ["name", "student_id", "grades"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        student_dict = Student.to_dict()
        writer.writerow(student_dict)
    students.append(student.to_dict())
    print(student.display())

def intro():
    print("=====================================\n\nSIMPLE GRADE BOOK\n\n=====================================\n\nWelcome to the Class Grade Book!\n")

def main_menu():
    choice = input("\nMAIN MENU\n[1] Add New Student\n[2] Add Grade to Student\n[3] View Student Record\n[4] View All Students\n[5] Class Summary\n[6] Exit\n\nEnter your choice (1-6): ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            add_new_student()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("\nExiting...")
            break
        else:
            print("\nInvalid Choice")

main()