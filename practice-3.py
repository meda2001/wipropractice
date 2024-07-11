# Built-in-functions
 
 
my_list = [1,2,3,4,5]
print(len(my_list))
 
 
my_string ="Hello"
print(len(my_string))
 
print(type(123))
print(type("Hello"))
print(type([1,2,3,4,5]))
 
 
num = 123
print(str(num))
 
boolean_value = True
print(str(boolean_value))
 
num_str = "123"
print(int(num_str))
 
 
num_float = 123.45
print(int(num_float))
 
 
for x in range(2,10,2):
    print(x)
   
   
   
# user-defined functions
 
def hello(name):
    print("Hello",name)
   
hello("Alice")
 
 
def add(a,b):
    return a+b
 
print(add(5,3))
 
 
# Recursive Function
 
 
# 0 1 1 2 3 5 8 13 ......
 
 
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
for i in range(10):
    print(fibonacci(i), end=" ")
   
   
# 5!   5*4*3*2*1
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
 
print(factorial(5)) 