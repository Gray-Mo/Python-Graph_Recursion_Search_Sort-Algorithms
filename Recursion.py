def factorial(num):
    if (num == 1):
        return 1
    else:
        return num * factorial(num-1)

def fibonacci(num):
    if (num <= 1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


num = 6
print(factorial(num))
print(fibonacci(num))