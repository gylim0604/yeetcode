import collections
import heapq


class NumberContainers:

    def __init__(self):
        self.num_map = {}
        self.indx_map = collections.defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.num_map[index] = number
        heapq.heappush(self.indx_map[number], index)
        
    def find(self, number: int) -> int:
        if not self.indx_map[number]:
            return -1
        
        while self.indx_map[number]:
            index = self.indx_map[number][0]

            if self.num_map.get(index) == number:
                return index
            
            heapq.heappop(self.indx_map)

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
obj = NumberContainers()
obj.change(1,10)
print(obj.find(10))