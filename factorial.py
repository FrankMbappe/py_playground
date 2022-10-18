def factorial_for(n):
    if n < 0:
        return "Invalid value, please provide a positive integer"
    if n == 0:
        return 1
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


def factorial_recur(n):
    if n < 0:
        return "Invalid value, please provide a positive integer"
    if n == 0:
        return 1
    return n * factorial_recur(n - 1)


print(factorial_for(int(input("Factorial (For) -> Enter a positive integer value : "))))
print(factorial_recur(int(input("Factorial (Recursive) -> Enter a positive integer value : "))))
