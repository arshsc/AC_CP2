names = ["Arsh", "Gov", "Isaac"]

names.append("Johann")

print(names)

print(names.sort())

for name in names:
    print(name)

list = [1,2,3,4,5]
list.append(1)
list.insert(2, 5)
list.remove(5)
list.pop()

print(list)

list.clear()
for num in enumerate(list):
    print(list)

if list == names:
    pass

print(len(list))

print(names[0])
combined_lists = list + names
names.index("Arsh")
text = "Hello World"
new_list = text.replace("World", "Hello")

file_path = "test"
# reading
def open_file():
    with open(file_path, 'r') as file:
        return file.read()

# write
with open(file_path, 'w') as file:
    pass

# append
with open(file_path, 'a') as file:
    pass

file_path.close()

# local and global is where a function can be accessed, local is in a funtion and global can be accessed anywhere
def func_test():
    var = 5

global var_two

def function_two(param1, param2):
    param1 += 1
    param2 -= 3

def function_three(param1=5):
    if 4 == 4:
        param1 +=4
        print(f"Added to {param1}")
        return param1
    else:
        return None
    
function_three(param1=6)

# good functions are shorter, effiecient, reaable, and reusable

# classes
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