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


# Task 2

def numbers():
    seq = [1, 2, 3]
    index = 0
    while True:
        yield seq[index]
        index = (index + 1) % len(seq)


try:
    count = int(input("How many numbers do you want to see? "))
    output = numbers()

    result = "-".join(str(next(output)) for _ in range(count))
    print(result)

except ValueError:
    print("Enter only numbers")
