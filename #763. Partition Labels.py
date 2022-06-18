class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        end = -1
        size = 0
        for j in range(len(s)):
            end = max(end, d[s[j]])
            if j == end:
                result.append(size+1)
                size = 0
                continue
            size += 1

        return result
