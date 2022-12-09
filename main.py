import math
import random as r, numbers
from school import student, numpy

from school.course import Course

student1 = student.Student('John Doe', 20, 'Computer Science', 'Science')
print(student1)

student2 = student.Student('Jane Doe', 21, 'Computer Science', 'Science')

course1 = Course('Python', 'John Doe')
course2 = Course('Java', 'Jane Doe')
course3 = Course('C++', 'John Doe')
student1.add_course(course1)
student1.add_course(course2)
student1.add_course(course3)
course1.add_student(student1)
course2.add_student(student1)
course3.add_student(student1)

student2.add_course(course1)
course1.add_student(student2)

course1.set_student_grade(student1, 90)
course1.set_student_grade(student2, 80)
course2.set_student_grade(student1, 70)
course3.set_student_grade(student1, 60)

print(student1.average_grade())
print()
print(course1.get_average_grade())

# if __name__ == '__main__':
#     main()