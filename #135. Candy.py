class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = [1 for i in range(len(ratings))]
        i = 1
        while i < len(ratings):
            if(ratings[i] > ratings[i-1]):
                l[i] = l[i-1]+1
            i += 1

        j = len(ratings)-2
        while(j >= 0):
            if(ratings[j] > ratings[j+1]):
                l[j] = max(l[j], l[j+1]+1)

            j -= 1

        sum = 0
        for k in l:
            sum += k

        return sum
