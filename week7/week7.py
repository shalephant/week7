def a1b2c3(x9):
    if x9 == 0 or x9 == 1:
        return 1
    else:
        return x9 * a1b2c3(x9 - 1)

if __name__ == "__main__":
    y7 = 5
    print(f"Factorial of {y7} is {a1b2c3(y7)}") 