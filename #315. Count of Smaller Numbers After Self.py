import bisect
from sortedcontainers import SortedList
def countSmaller(nums):
    s1=SortedList()
    ans=[]

    for num in reversed(nums):
        i=s1.bisect_left(num)
        ans.append(i)
        print(ans)
        s1.add(num)
        print("S1",s1)

    return ans[::-1]

print(countSmaller([2, 5,6, 1]))
