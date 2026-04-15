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

print(triangular(6))