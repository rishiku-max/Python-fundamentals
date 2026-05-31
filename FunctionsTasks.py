# 1. Write a function greet() that prints "Hello, Python Learner!" 
def greet():
    print("Hello, Python Learners! ")

greet()

# 2. Write a function square(num) that returns the square of a given number. Test it with different numbers.
def square(num):
    return num*num
num = int(input("enter a no. "))
sq = square(num)
print(sq)



# 3. Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last"

def full_name(first, last):
    print(first + last)

first = input("enter first name: ")
last  = input("enter last name: ")
full_name(first, last)


# 4. Write a function a rectangle. Test it by calling the function with: 
# 	A. Both calculate_area(length, width=10) that returns the area of length and B. Only width length (use default width)
def calculate_area(length, width = 10):
    print("area = ", length*width)
def rectangle():
    l = int(input("enter length : "))
    b = int(input("enter width : "))
    calculate_area(l,b)
    calculate_area(l)

rectangle()


# 5. Create a list and use map() to create a table of n by using lambda function.

n = int(input("Enter number: "))

nums = [1,2,3,4,5,6,7,8,9,10]

table = list(map(lambda x: x * n, nums))

print("Table of", n, "is:")
print(table)



# 6. Write a lambda function that adds two numbers and test it.

a = 20
b = 25
C = lambda a,b: a+b
print(C(a,b))


# 7. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, nums))

print(squares)

# 8. Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

def fibo(n):
    if (n==1 or n==2):
     return 1
    return fibo(n-1)+fibo(n-2)


res = fibo(8)
print(res)



# 9. Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))




# 10. Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
#



# 11. Write a function increment() that has a local variable 0 and increments it by counter initialized to 1 each time it is called. Observe whether the value persists across function calls.

def increment():
    counter = 0
    counter = counter + 1
    print(counter)

increment()
increment()
increment()






# 12. Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring

def multiply(a, b):
    """
    multiply(a, b)

    This function takes two numbers as input
    and returns their multiplication result.
    """
    return a * b


# calling function
result = multiply(5, 4)
print("Result:", result)

# showing docstring
help(multiply)





# 13.Find the square root of 144

import math

result = math.sqrt(144)

print(result)




# 14. Calculate sin(90°) (hint: use math.radians())
# convert degrees to radians
angle = math.radians(90)
# calculate sine value
result = math.sin(angle)
print("sin(90°) =", result)




# 15. Create your own module and import module by using (as) keyword and use all the functions of that module into your base program.




