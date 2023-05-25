target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


def carFleet():
    pairs = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pairs)[::-1]:
        TIME = (target - p) / s
        stack.append(TIME)
        if len(stack) > 1 and TIME <= stack[-2]:
            stack.pop()

    return len(stack)


print(carFleet())
