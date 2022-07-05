class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        boxes = 0
        for i in boxTypes:
            if((boxes+i[0]) <= truckSize):
                units += i[0]*i[1]
                boxes += i[0]

            else:
                units += (truckSize-boxes)*i[1]
                boxes += (truckSize-boxes)

        return units
