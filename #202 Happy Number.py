def isHappy(n):
    def get_num(n):
        sum = 0
        while n > 0:
            digit = n % 10
            n = n//10
            sum += digit*digit
        return sum
    values = []
    while n != 1 and n not in values:
        values.append(n)
        n = get_num(n)
    return n == 1


isHappy(19)
