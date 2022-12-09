class Course:
    def __init__(self, name, teacher, students = []):
        self.name = name
        self.teacher = teacher
        self.students = students
        self.grades = {}

    def add_student(self, student):
        self.students.append(student)
        self.grades[student.name] = 0

    def remove_student(self, student):
        self.students.remove(student)
        self.grades.pop(student.name)

    def get_average_grade(self):
        value = 0
        for student in self.students:
            print(student.name, self.grades[student.name])
            value += self.grades[student.name]
        return value / len(self.students)
    
    def set_student_grade(self, student, grade):
        self.grades[student.name] = grade
    
    def get_student_grade(self, student):
        return self.grades[student.name]

def util():
    print('util')

name = 'main'