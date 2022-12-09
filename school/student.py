class Student:
    def __init__(self, name, age, department, faculty) -> None:
        self.name = name
        self.age = age
        self.department = department
        self.faculty = faculty
        self.courses = []

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old, studying {self.department} in {self.faculty}'

    def __repr__(self) -> str:
        return f'{self.name} is {self.age} years old, studying {self.department} in {self.faculty}'

    def __add__(self, other):
        return self.age + other.age

    def add_course(self, course):
        self.courses.append(course)
        course.add_student(self)

    def remove_course(self, course):
        self.courses.remove(course)
        course.remove_student(self)
    
    def get_courses(self):
        return self.courses
    
    def set_courses(self, courses):
        self.courses = courses

    def average_grade(self):
        value = 0
        for course in self.courses:
            value += course.get_student_grade(self)
        return value / len(self.courses)

    def __setattr__(self, __name: str, __value) -> None:
        if __name == 'age':
            if __value < 18:
                raise ValueError('Student must be 18 years or older')
        super().__setattr__(__name, __value)

        if __name == 'courses':
            if len(__value) > 5:
                raise ValueError('Student can only take 5 courses')
    
    def __getattribute__(self, __name: str):
        if __name == 'courses' or __name == 'age':
            return super().__getattribute__(__name)

        return super().__getattribute__(__name)
