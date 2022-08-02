class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefix = []
        self.product = 1

    def add(self, num: int) -> None:
        self.stream.append(num)
        if num != 0:
            self.product = num*self.product
            self.prefix.append(self.product)

        else:
            self.prefix = []
            self.product = 1

    def getProduct(self, k: int) -> int:
        if(len(self.prefix) < k):
            return 0
        elif(k == len(self.prefix)):
            return self.prefix[-1]
        else:
            return int(self.prefix[-1]/self.prefix[-1-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
