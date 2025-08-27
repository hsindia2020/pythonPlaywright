aa = [2,3,5,7,8,9]
aalen = aa.__len__
revSort = aa.sort(reverse=True)

for i in aa:
    print(i, " Index ", aa.index(i))
    aa.remove(i) # remove element from list in loop
    if i == 7:
        break
    elif i == 5: # type: ignore
        print("In else")    
    
print("Lenght: ",aalen())
# commonfile.py
# This file can contain common functions, classes, or variables
# that can be imported and used in other Python files.
# For example:
def common_function():
    print("This is a common function from commonfile.py")
def add(a, b):
    print(a + b)
add(3,5)
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def modulus(a, b):
    return a % b
def exponent(a, b):
    return a ** b
def floor_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot divide by zero"
def max_of_two(a, b):
    return a if a > b else b
def min_of_two(a, b):
    return a if a < b else b
def is_even(n):
    return n % 2 == 0
def is_odd(n):
    return n % 2 != 0
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
