class ProductOfNumbers:

    def __init__(self):
        self.prefix_stream = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_stream = [1]
            self.size = 0
        else:
            self.prefix_stream.append(self.prefix_stream[self.size]*num)
            self.size+=1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (self.prefix_stream[self.size]// self.prefix_stream[self.size-k])
# Your ProductOfNumbers object will be instantiated and called as such:
sol = ProductOfNumbers()
sol.add(3)
sol.add(0)
sol.add(2)
sol.add(5)
sol.add(4)
print( sol.getProduct(2))
print(40//10)