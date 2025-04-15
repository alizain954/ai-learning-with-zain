#function
def add_number(a, b):
    return a+b

result = add_number(5, 12)
print(result)

#default parameter

def MyName(name='zain'):
    return (f'hello malik {name}')
    
result = MyName()
print(result)
result = MyName('ALi')
print(result)

# Task 1 Write a function to check if a number is even or odd.

def is_even(num):
    if num % 2 ==0:
        return 'Even'
    else:
        return 'Odd'

result = is_even(13)
print(result)

#Write a function to calculate factorial of a number

def cal_factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result
result = cal_factorial(5)
print(result)


#lambda Function 
# the function which have no name 
show = lambda x : x+5

print(show(5))

# Assigment You are given a list of integers. Square each number using map() and lambda.

numbers = [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]

a = list(map(lambda x:x**2, numbers))
print(a)

# Assigmet 2 From a list of integers, filter out only even numbers.
numbers = [10, 15, 20, 25, 30, 35]
# Expected Output: [10, 20, 30]

b = list(filter(lambda x: x%10 ==0, numbers))
print(b)

# Assigment 3.Given a list of numbers, use reduce() to calculate the product of all elements.

numbers = [1,2,3,4,5]
from functools import reduce

d = reduce(lambda x, y:x*y, numbers)
print(d)