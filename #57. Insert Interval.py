class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        LENGTH = len(intervals)
        nonOverlappingIntervals = []

        for i in range(LENGTH):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                nonOverlappingIntervals.append(newInterval)
                return nonOverlappingIntervals+intervals[i:]
            elif newInterval[0] > interval[1]:
                nonOverlappingIntervals.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]),
                               max(interval[1], newInterval[1])]

        nonOverlappingIntervals.append(newInterval)
        return nonOverlappingIntervals