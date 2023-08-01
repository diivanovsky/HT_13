# 1 Task

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


try:
    limit = int(input("How many numbers? "))
    if limit <= 0:
        raise ValueError("It must be positive")

    sequence = fib(limit)
    for number in sequence:
        print(number)

except ValueError as ve:
    print("Error:", ve, "Enter only numbers")