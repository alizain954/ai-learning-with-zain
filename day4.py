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