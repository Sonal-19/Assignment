""" 1)Palindrome Program In Python"""
def ispalindrome(s):
    return s == s[ : : -1]
s = "mam"
s = ispalindrome(s)
if s:
    print("yes")
else:
    print("no")

"""2)Factorial Program In Python"""
num = int(input("enter a number: "))
factorial = 1
if num < 0:
    print("factorial does not exist for negative number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("the factorial of", num, "is", factorial)

import math
def fact(n):
    return(math.factorial(n))
num = int(input("enter the number:"))
f = fact(num)
print("factorial of", num, "is", f)

"""3)Fibonacci Series Program"""
def fabonacci(n):
    if n > 0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print (fibonacci(9))


"""4. Armstrong Number Program In Python"""
num = int(input("enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is Armstrong number")
else:
    print(num, "is not an Armstrong number")

"""5. Calculator Program"""
x = int(input("enter first number: "))
y = int(input("enter second number: "))
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("enter choice(1/2/3/4): ")

"""6. Patterns Program In Python"""
for x in range(5):
    for y in range(5-x):
        print("*", end = " ")
    print()


"""7. Leap Year Program"""
def check_leap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print("given year is a leap year")
    else:
        print("given year is not a leap year")
year = int(input("enter the number: "))
check_leap(year)

"""8. Prime Number Program In Python++"""
def prime_checker(a):
    if a > 1:
        for j in range(2, int(a/2)+1):
            if (a % j) == 0:
                print(a, "is not a prime number")
                break
            else:
                print(a, "is a prime number")
    
a = int(input("enter a number: "))
prime_checker(a)

"""9. Program To Find Area In Python"""
a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("the area of the triangle is %0.2f" %area)

"""10.Program To Reverse A List"""
list = [5, 6, 7, 8, 9, 34, 56]
list.reverse()
print("using reverse()", list)
print("using reversed()", list(reversed(list)))

"""11.Program to find sum of all elements in list"""
def sumlist(list):
    sum = 0
    for i in range(len(list)):
        sum = sum+list[i]
    return sum
list = [11,4,6,8]
print(list)
print("sum of list: ",sumlist(list))

"""12.Find average, max, min of list elements"""
list = [1,2,3]
minimum = min(list)
maximum = max(list)
sum = sum(list)
length = len(list)
average = sum/length
print(average)

"""13.Write a Python program to create a dictionary grouping a sequence of key value pairs into a dictionary of lists.
a. Original list:[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}"""
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))


"""14. Write a Python program to convert more than one list to nested 
dictionary.
a. Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary: [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': 
{'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]"""
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))


"""15. Python program to check if a set is a subset of another set."""
a = {1,2,3}
b = {1,2,3,4,5}
print(a.issubset(b))

"""16.Write a Python program to create a symmetric difference and set 
difference"""
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
result = A.symmetric_difference(B)
print(result)

"""17.Write a Python program to remove an empty tuple(s) from a list of tuples.
a. Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']"""
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


"""18. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
a. Original Tuple: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:[30.5, 34.25, 27.0, 23.25]"""
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result
nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))


""""19)Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters"""
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")