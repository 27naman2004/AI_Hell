# contorl structue 

# conditional statement

x=10
if(x>0):
    print("Positive")
elif(x==0):
    print("Zero")
else:
    print("Negative")

# loops
# for loop
for i in range(5):
    print(f"iteration: {i}")

# while loop
i = 0
while(i<5):
    print(f"iteration: {i}")
    i+=1

# break and continue
for i in range(10):
    if(i==5):
        break
    print(f"iteration: {i}")

for i in range(10):
    if(i==5):
        continue
    print(f"iteration: {i}")

# nested loop
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# pass
for i in range(5):
    pass
print("End of loop")

# match-case statment (python 3.10)\
# match-case is similar to switch-case in other programming languages
x = 10
match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")


# else with while loop
i = 0
while(i<5):
    print(f"iteration: {i}")
    i+=1
else:
    print("End of loop")

# else with for loop
for i in range(5):
    print(f"iteration: {i}")
else:
    print("End of loop")

# infinite loop
while True:
    print("Infinite loop")
    
