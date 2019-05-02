#  Finds the Nth number in the sequence

fib = {}

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib[n] = fibonacci(n-1) + fibonacci(n-2)
        print(f"fib[{n}]:", fib[n])
    return fib[n]

    #return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fib)