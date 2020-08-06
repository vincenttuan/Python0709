def add(x):
    return x + 1

def sub(y):
    return y - 1

def operator(func, n):
    if (n < 200):
        n = 200
    return func(n)

if __name__ == '__main__':
    print(operator(add, 50))
    print(operator(add, 250))
    print(operator(sub, 70))
    print(operator(sub, 700))
