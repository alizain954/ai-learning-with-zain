# we will learn the comparison operator nd also the logic (if else)

num = 80
if num <= 85:
    print('good')
    
#Now we use the if and else

num = 75

if num >= 80:
    print('Grade is A+')
else:
    print('less then Grade A+')
    
#Now we are moving in the if-elif-else

num = 80
if num >= 90:
    print('Grade is A+')
elif num >= 75:
    print('Grade B+')
elif num >= 50:
    print('Pass')
else:
    print('Fail')
    
# now moving to input field:

name = input('Enter the name: ')
if name == 'zain':
    print('Hello' + name)
else:
    print('Hello Guest')
    
# now moving to the comparison operator:

a = 100
b = 50

print('a==b', a==b) # False a and b are not equcal
print('a>b', a>b) # True a is gretar than b
print('a<b', a<b) # False a is not less than b
print('a>=b', a>=b) # True a is gretaer than equcal to b
print('a<=b', a<=b) #False a is not less than equcal to b