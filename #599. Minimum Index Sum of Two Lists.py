class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sum = float("inf")
        result = []
        for i in range(len(list1)):
            if(list1[i] in list2):
                iDx = list2.index(list1[i])
                if(i+iDx == sum):
                    sum = i+iDx
                    result.append(list1[i])
                elif(i+iDx < sum):
                    if result:
                        result.pop(-1)
                    sum = i+iDx
                    result.append(list1[i])

        return result
