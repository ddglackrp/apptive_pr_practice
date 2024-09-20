def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def pow(a, b):
    return a ** b

def abs(a):
    return a if a >= 0 else -a

def mod(a, b):
    return a % b

if __name__ == "__main__":
    # 간단한 테스트 코드
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
    print("Power:", pow(2, 3))
    print("Absolute:", abs(-10))
    print("Modulus:", mod(10, 3))
