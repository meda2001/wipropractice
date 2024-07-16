class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def get_details(self):
        return str(self)

class Student(Person):
    school_name = "Greenwood High School"
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
    
    def get_courses(self):
        return ", ".join([course.name for course in self.courses])
    
    def get_details(self):
        return f"{super().get_details()}, Student ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses_teaching = []
    
    def assign_course(self, course):
        self.courses_teaching.append(course)
    
    def get_courses_teaching(self):
        return ", ".join([course.name for course in self.courses_teaching])
    
    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.employee_id}"

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def __str__(self):
        return f"{self.name} ({self.code})"


class School:
    name = "Greenwood High School"
    
    @classmethod
    def get_school_name(cls):
        return cls.name
    
    @staticmethod
    def is_school_day(day):
        return day.weekday() < 5  # Monday to Friday are school days
