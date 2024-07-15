# classes and Objects
# class : like a blueprint for creating objects . (properties and behaviors )
# Object : instance of a class
 
 
class Dog:
    species = "Canis familiaris"
   
    def __init__(self , name , age):
        self.name = name
        self.age = age
       
    def description(self):
        return f"{self.name} is {self.age} years old"
   
    def speak(self , sound):
        return f"{self.name} says {sound}"
   
   
buddy = Dog('Buddy',9)
miles = Dog('Miles',4)
 
print(buddy.name)
print(miles.age)
 
 
print(buddy.description())
print(miles.speak("Woof woof"))
 
 
 
class Car:
    wheels = 4
   
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
       
       
    def description(self):
        return f"{self.year} {self.make} {self.model}"
   
    def start_engine(self):
        return f"{self.description()} engine started!"
   
   
car1 = Car("Toyota","Camry",2020)
car2 = Car("Honda","Accord",2021)
 
print(car1.make)
print(car2.model)
 
print(car1.description())
print(car2.start_engine())
 