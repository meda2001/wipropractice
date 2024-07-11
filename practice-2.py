def hello(name="Unkown"):
    print("Hello",name)
   
   
hello("Alice")
hello("Peter")
 
 
 
def sum2(num1 , num2):
    return num1+num2
   
   
res1 = sum2(5,2)
res2 = sum2(10,12)
print(res1*res2)
 
print(pow(2,3))
 
 
import math
print(math.sqrt(9))
 
 
hello()
 
 
 
def sumN(*nums):
    res=0
    for num in nums:
        res+=num
    print(res)
   
 
 
sumN() # 0
sumN(2) # 2
sumN(2,3)  # 5
sumN(2,3,4,5)  # 14
 
 
favDay="Sunday"
def func1():
    day="Thursday"
    print(favDay)
    print(day)
 
print(favDay)
func1()
