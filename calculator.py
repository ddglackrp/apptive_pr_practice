def add(a, b):
    return a+b


def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b


def divide(a, b):
    if b==0:
        return "error"
    return a/b


def pow(a, b):
    return a**b


def abs(a):
    return a if a>=0 else -a

def mod(a, b):
    return a%b

if __name__ == "__main__":
    # 간단한 테스트 코드
    print("Addition:", add(5, 3))        # 8
    print("Subtraction:", subtract(5, 3))  # 2
    print("Multiplication:", multiply(5, 3))  # 15
    print("Division:", divide(5, 0))      # Error: Division by zero
    print("Power:", pow(5, 3))            # 125
    print("Absolute:", abs(-5))           # 5
    print("Modulus:", mod(5, 3))          #2