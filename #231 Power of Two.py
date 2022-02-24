import math


def isPowerOfTwo(n):
    if n == 1:
        return True
    elif(n % 2 != 0):
        return False
    else:
        for i in range(0, math.ceil(abs(n)**(1/2))+1):
            if n == 2**i:
                return True
        return False


isPowerOfTwo(8)
