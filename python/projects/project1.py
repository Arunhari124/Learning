import json
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of 3 marks [3, 3, 4] style

    def get_total(self):
        return sum(self.marks)

    def get_average(self):
        return self.get_total() / len(self.marks)

    def get_grade(self):
        total = self.get_total()
        if total >= 7:
            return "A"
        elif total >= 4:
            return "B"
        else:
            return "C"

    def show_info(self):
        print(f"Name: {self.name} | Total: {self.get_total()} | Average: {self.get_average():.2f} | Grade: {self.get_grade()}")


# list to store student objects
students_list = []



# ---- ADDING STUDENTS ----
is_running = True
while is_running:
    stop = input("Enter 1 to add student or 0 to stop: ")

    if stop == "0":
        is_running = False
    else:
        name = input("Enter student name: ")

        marks = []
        for i in range(1, 4):
            mark = int(input(f"Enter mark of subject {i}: "))
            marks.append(mark)

        # create a Student object and add to list
        student = Student(name, marks)
        students_list.append(student)
        print(f"{name} added!\n")


# ---- SHOW ALL STUDENTS ----
print("\n______ STUDENT INFO ______")
for student in students_list:
    student.show_info()

# ---- TOPPER ----
topper = students_list[0]
for student in students_list:
    if student.get_total() > topper.get_total():
        topper = student

print(f"\nTopper: {topper.name} with total {topper.get_total()}")

with open('student.json', 'w') as file:
    json.dump(students_list, file)
with open('student.json', 'r') as file:
    data = json.load(file)
print(data)