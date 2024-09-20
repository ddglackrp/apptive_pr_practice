def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 
    return a / b

def pow(a, b):
    return a ** b

def abs(a):
    return a if a >= 0 else -a

def mod(a, b):
    return a % b

if __name__ == "__main__":
    print(add(10, 5))        
    print(subtract(10, 5))   
    print(multiply(10, 5))   
    print(divide(10, 5))     
    print(pow(2, 3))         
    print(abs(-10))         
    print(mod(10, 3))        
