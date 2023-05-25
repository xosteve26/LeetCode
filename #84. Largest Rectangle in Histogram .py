heights = [2, 1, 5, 6, 2, 3]
monotonicDecreasingStack = []
largestRectangularHistogram = 0


def largestHistogram():
    global largestRectangularHistogram
    for i in range(len(heights)):
        start = i
        while monotonicDecreasingStack and heights[i] < monotonicDecreasingStack[-1][1]:
            idx, height = monotonicDecreasingStack.pop()
            largestRectangularHistogram = max(largestRectangularHistogram, height * (i - idx))
            start = idx

        monotonicDecreasingStack.append((start, heights[i]))

    while monotonicDecreasingStack:
        ix, h = monotonicDecreasingStack.pop()
        largestRectangularHistogram = max(largestRectangularHistogram, h * (len(heights) - ix))

    return largestRectangularHistogram


print(largestHistogram())
