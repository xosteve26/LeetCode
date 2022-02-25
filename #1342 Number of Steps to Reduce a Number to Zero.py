def nos(num):
    return helper(num, 0)


def helper(num, count):
    if(num % 2 == 0):
        num /= 2
        count += 1
    else:
        num -= 1
        count += 1

    if num == 0:
        return count

    return helper(num, count)


print(nos(14))
