def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 8
print(f"Factorial of {num} is {factorial(num)}")
