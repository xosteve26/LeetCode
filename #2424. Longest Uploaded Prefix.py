class LUPrefix:

    def __init__(self, n: int):
        self.LONGEST = [False]*(n+1)
        self.MAX = 1
        self.LENGTH = n+1

    def upload(self, video: int) -> None:
        self.LONGEST[video] = True

        while self.MAX < self.LENGTH and self.LONGEST[self.MAX]:
            self.MAX += 1

    def longest(self) -> int:
        return self.MAX-1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
