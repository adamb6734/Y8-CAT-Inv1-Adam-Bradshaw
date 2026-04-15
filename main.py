#fractal trees

def startriangle(n):
    if n > 0:
        print("*" * n)
        startriangle(n-1)

startriangle(5)