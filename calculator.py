def add(a, b):
    print(a+b)


def subtract(a, b):
	print( a-b )


def multiply(a, b):
    print( a*b)


def divide(a, b):
    print( a/b)


def pow(a, b):
    print( a**b)


def abs(a):
    if a > 0 :
        print( a)
    else :
        print( -a)


def mod(a, b):
    print( a%b)



if __name__ == "__main__":
    # 간단한 테스트 코드
    add(1,2)
    subtract(3,2)
    multiply(3,4)
    divide(8,2)
    pow(9,3)
    abs(5)
    mod(8,3)