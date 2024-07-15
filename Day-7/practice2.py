class Employee:
    # class variable
    company_name = "TechCorp"
   
    def __init__(self,name,salary):
        # Instance variables
        self.name = name
        self.salary = salary
       
    # Instance method
    def employee_details(self):
        return f"Name: {self.name} , Salary: {self.salary}"
   
    # class method
    @classmethod
    def company_details(cls):
        return f"Company : {cls.company_name}"
   
    # static method
    @staticmethod
    def is_working_day(day):
        return day.weekday() < 5
   
emp1 = Employee("Alice",70000)
emp2 = Employee("Bob",80000)
 
 
print(emp1.employee_details())
print(emp2.employee_details())
 
 
 
from datetime import datetime
print(Employee.company_details())
print(Employee.is_working_day(datetime(2024,7,15)))