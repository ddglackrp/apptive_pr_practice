def add(a, b):
    return a+b


def subtract(a, b):
	return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def pow(a, b):
    return a**b


def abs(a):
    if a < 0:
        return a*-1
    else:
        return a

def mod(a, b):
    return a%b


if __name__ == "__main__":
    a=3
    b=2
    print(add(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))
    print(pow(a, b))
    print(abs(a))
    print(mod(a, b))
