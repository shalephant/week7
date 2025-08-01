def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))


def f(n):
    s = []
    x1, x2 = 0, 1
    for _ in range(n):
        s.append(x1)
        x1, x2 = x2, x1 + x2
    return s

print(f(10))