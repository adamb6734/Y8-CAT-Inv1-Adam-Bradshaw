#fractal trees

def startriangle(n):
    if n > 0:
        print("*" * n)
        startriangle(n-1)

# startriangle(5)

def triangular(n):
    if n == 0:
        return 0
    else:
        return n + triangular(n-1)

#print(triangular(6))

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))