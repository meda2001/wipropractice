class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def get_details(self):
        return str(self)


class Member(Person):
    library_name = "City Library"
    
    def __init__(self, name, age, member_id):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def get_borrowed_books(self):
        return ", ".join([book.title for book in self.borrowed_books])
    
    def get_details(self):
        return f"{super().get_details()}, Member ID: {self.member_id}"


class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.assigned_books = []
    
    def assign_book(self, book):
        self.assigned_books.append(book)
    
    def get_assigned_books(self):
        return ", ".join([book.title for book in self.assigned_books])
    
    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.employee_id}"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    name = "City Library"
    
    @classmethod
    def get_library_name(cls):
        return cls.name
    
    @staticmethod
    def is_open(day):
        return day.weekday() < 5  # Monday to Friday are open days
