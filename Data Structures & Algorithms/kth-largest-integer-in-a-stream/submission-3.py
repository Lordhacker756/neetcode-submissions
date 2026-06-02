import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for i in nums:
            heapq.heappush(self.heap, -i)
        self.k = k       

    def add(self, val: int) -> int:
        temp = []
        heapq.heappush(self.heap, -val)
        for i in range(self.k):
            temp.append(heapq.heappop(self.heap))
        
        res = temp[-1]

        for i in temp:
            heapq.heappush(self.heap, i)
        return -res
