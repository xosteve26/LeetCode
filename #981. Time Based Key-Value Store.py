class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l,r=0,len(self.map[key])-1
        VALUES=self.map[key]
        RESULT=""
        while l<=r:
            mid=(l+r)//2
            TS=VALUES[mid][1]
            if(TS<=timestamp):
                RESULT= VALUES[mid][0]
                l=mid+1
            else:
                r=mid-1

        return RESULT















# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)