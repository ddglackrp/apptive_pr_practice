def add(a, b):
    return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def pow(a, b):
    return a ** b


def abs(a):
    if a < 0:
         return -a
    return a


def mod(a, b):
    return a % b


if __name__ == "__main__":
    print(add(1,2))
    print(subtract(1,2))
    print(multiply(1,2))
    print(divide(1,2))
    print(pow(1,2))
    print(abs(-1))
    print(mod(1,2))
    