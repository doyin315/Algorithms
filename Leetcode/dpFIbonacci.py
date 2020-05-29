def fibonacci(n,cache={}):
    if n<=1:
        return n
    cache[n] = fibonacci(n-1) + fibonacci(n-2)

    return cache[n]

print(fibonacci(6))