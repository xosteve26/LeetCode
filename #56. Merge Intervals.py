class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        LENGTH = len(intervals)
        if LENGTH == 1:
            return intervals

        intervals.sort()
        nonOverlappingIntervals = []
        movingInterval = intervals[0]

        for i in range(1, LENGTH):
            interval = intervals[i]
            if interval[0] > movingInterval[1]:
                nonOverlappingIntervals.append(movingInterval)
                movingInterval = interval
            elif interval[1] < movingInterval[0]:
                nonOverlappingIntervals.append(interval)
            else:
                movingInterval = [min(interval[0], movingInterval[0]), max(
                    interval[1], movingInterval[1])]

        nonOverlappingIntervals.append(movingInterval)

        return nonOverlappingIntervals
