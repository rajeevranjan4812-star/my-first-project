x = int(input("enter the number "))
y = int(input("enter the number "))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial of {x} is {factorial(x)}")
print(f"Factorial of {y} is {factorial(y)}")
