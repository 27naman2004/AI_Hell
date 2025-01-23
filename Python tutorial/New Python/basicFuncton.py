# basic function

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):  
    return a % b

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

def even_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
            
def odd_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i)

def prime_numbers(a, b):
    for i in range(a, b + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)

def fibonacci_series(a):
    n1 = 0
    n2 = 1
    count = 0
    if a <= 0:
        print("Please enter a positive integer")
    elif a == 1:
        print("Fibonacci sequence upto", a, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < a:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

def outer_function():
    x = 300
    def inner_function():
        print(x)
    inner_function()

print(add(5, 3))
print(sub(5, 3))
print(mul(5, 3))
print(div(5, 3))
print(mod(5, 3))
print(factorial(5))
even_numbers(5, 10)
odd_numbers(5, 10)
prime_numbers(5, 10)
fibonacci_series(10)

outer_function()
    