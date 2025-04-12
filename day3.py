# loop
fruit = ['ali', 'zain', 'adnan', 'epazz', 'trump']
for i in fruit:
    print(i)

# Range
for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)
    
#while Loop

x = 5
i = 0
while i <= x:
    print(i)
    i += 1
    
# Break and continue

for i in range(1 , 10):
    print(i)
    if i == 5:
        break

for i in range(1 , 10):
    
    if i == 5:
        continue
    print(i)


for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Square Star
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

#Triangle Star pattern

for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print()