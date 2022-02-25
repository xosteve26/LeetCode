# def rec(n):
#     if(n == 0):
#         return
#     print(n)
#     rec(n-1)
#     print(n)


# rec(5)


# def fact(i):
#     if(i == 1):
#         return 1
#     return i*fact(i-1)


# fact(5)

# def sumN(num):
#     dig = num % 10
#     num //= 10
#     if num == False:
#         return dig
#     return dig + sumN(num)


# sumN(314)


# def rev(num):
#     dig = num % 10  # 4 #1 #3
#     num //= 10  # 31 #3
#     if(num == False):
#         return str(dig)

#     return str(dig) + rev(num)


# def palindrome(num):
#     return num == int(rev(num))


# palindrome(12134)


# def c0(num, count):
#     dig = num % 10
#     num //= 10

#     if num == False:
#         return count

#     if(dig == 0):
#         return c0(num, count+1)
#     return c0(num, count)


# print(c0(1200900, 0))
