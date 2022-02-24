
def checkPerfectNumber(num):
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum += i
        if sum == num:
            return print("True")
    return print("False")


checkPerfectNumber(30402457)
