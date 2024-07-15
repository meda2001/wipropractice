# Inheritance
# allows a class to inherit attributes and methods from another class
# A(parent or base) ----> B(child or derived)
 
# Parent class
class Animal:
    def __init__(self,name):
        self.name = name
       
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
   
   
# child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
   
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
   
   
dog = Dog("Buddy")
cat = Cat("Whiskers")
 
 
print(dog.speak())
print(cat.speak())
 
 
 
 
 
# Parent Class
class Shape:
    def __init__(self,color):
        self.color=color
   
    def area(self):
        raise NotImplementedError("Subclass must implememt abstract method")
   
    def __str__(self):
        return f"A {self.color} shape"
   
   
# Child class
class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius
       
    def area(self):
        return 3.14 * self.radius * self.radius
   
    def __str__(self):
        return f"A {self.color} circle with radius {self.radius}"
   
   
class Rectangle(Shape):
    def __init__(self,color , width , height):
        super().__init__(color)
        self.height = height
        self.width = width
       
    def area(self):
        return self.width * self.height
   
    def __str__(self):
        return f"A {self.color} rectangle with {self.width} and height {self.height}"
   
   
   
circle = Circle("red",5)
rectangle = Rectangle("blue",4,6)
 
 
print(circle.area())
print(rectangle.area())
 
print(circle)
print(rectangle)