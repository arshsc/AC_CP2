# import needed libraries
import csv

# csv file
student_file = "individual_projects/grade_book/docs/students.csv"

# classes
# student class
class Student:
    # initalize name, student id, and grades as list
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = int(student_id)
        self.grades = []

    # add grade
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("\nGrade must be between 0 and 100.")

    # get grade average
    def grade_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # determine letter grade
    def letter_grade(self):
        avg = self.grade_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    # to display neatly
    def display(self):
        if len(self.grades) == 0:
            grades_display = "None yet"
        else:
            grades_display = self.grades
        return (
            f"Name: {self.name}\n"
            f"ID: {self.student_id}\n"
            f"Grades: {grades_display}\n"
            f"Average: {self.grade_average():.2f}\n"
            f"Letter Grade: {self.letter_grade()}"
        )

    # add to csv
    def to_csv_row(self):
        grades_str = ",".join([str(g) for g in self.grades])
        return {"name": self.name, "student_id": self.student_id, "grades": grades_str}

    # turn row into student
    @staticmethod
    def from_csv_row(row):
        student = Student(row["name"], row["student_id"])
        if row["grades"]:
            student.grades = [float(g) for g in row["grades"].split(",")]
        return student

# gradebook class
class GradeBook:
    # initalize students
    def __init__(self):
        self.students = []

    # add a student and save to csv
    def add_student(self, student):
        self.students.append(student)
        self.save_to_csv()

    # find a student by their id
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == int(student_id):
                return student
        return None

    # find a student by their name
    def find_student_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    # save to csv
    def save_to_csv(self):
        with open(student_file, "w", newline="") as file:
            fieldnames = ["name", "student_id", "grades"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.students:
                writer.writerow(student.to_csv_row())

    # load from csv
    def load_from_csv(self):
        try:
            with open(student_file, "r") as file:
                reader = csv.DictReader(file)
                self.students = [Student.from_csv_row(row) for row in reader]
        except:
            self.students = []


# functions
# add new student
def add_new_student(gradebook):
    print("\n=====================================\nADD NEW STUDENT\n=====================================")
    name = input("\nEnter student name: ").title()

    while True:
        student_id = input("Enter student ID: ")
        # check if student id is digits
        if student_id.isdigit():
            break
        print("\nInvalid ID. Must be a number.")

    # use the student and gradebook classes
    student = Student(name, student_id)
    gradebook.add_student(student)
    print("\nStudent added successfully!")
    # display the students info
    print(student.display())

# add grade to student
def add_grade_to_student(gradebook):
    print("\n=====================================\nADD GRADE\n=====================================")
    # if no students are in the gradebook
    if not gradebook.students:
        print("\nNo students in the gradebook yet.")
        return

    # print each student
    print("\nCurrent Students:")
    for student in gradebook.students:
        print(f"- {student.name} ({student.student_id})")

    student_id = input("\nEnter student ID to add grade: ")
    student = gradebook.find_student_by_id(student_id)

    if student:
        while True:
            try:
                grade = float(input(f"Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    student.add_grade(grade)
                    gradebook.save_to_csv()
                    print("\nGrade added successfully!")
                    print(f"{student.name} now has {len(student.grades)} grade(s)")
                    print(f"Current average: {student.grade_average():.1f} ({student.letter_grade()})\n")
                    break
                else:
                    print("\nGrade must be between 0 and 100.")
            except:
                print("\nInvalid input. Enter a number.")
    else:
        print("Student not found.")

# view student record
def view_student_record(gradebook):
    print("\n=====================================\nVIEW STUDENT RECORD\n=====================================")
    # display current students
    print("\nCurrent Students:")

    for student in gradebook.students:
        print(f"- {student.name} ({student.student_id})")

    student_id = input("\nEnter student ID to view: ")
    student = gradebook.find_student_by_id(student_id)

    if student:
        print("\n")
        print(student.display())
    else:
        print("Student not found.")

# view all students
def view_all_students(gradebook):
    print("\n=====================================\nALL STUDENTS\n=====================================")
    # if no students are in gradebook
    if not gradebook.students:
        print("\nNo students in gradebook.")
        return
    
    print("-------------------------")

    # display all the students
    for student in gradebook.students:
        print(student.display())
        print("-------------------------")
    
    # total amount of students
    print(f"Total students: {len(gradebook.students)}")

# class summary
def class_summary(gradebook):
    print("\n=====================================\nCLASS SUMMARY\n=====================================")
    # if no students are in gradebook
    if not gradebook.students:
        print("\nNo students in gradebook.")
        return
    
    # print each student with their average and letter grade
    print("\n")
    for student in gradebook.students:
        print(f"{student.name}: Average = {student.grade_average():.2f}, Letter Grade = {student.letter_grade()}")

# intro
def intro():
    print("=====================================\nSIMPLE GRADE BOOK\n=====================================\n\nWelcome to the Class Grade Book!")