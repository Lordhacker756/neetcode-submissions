import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res=[]

        for s in stones:
            res.append(-s)

        heapq.heapify(res)

        while(len(res)>1):
            s_a = heapq.heappop(res)
            s_b = heapq.heappop(res)

            diff = abs(s_a-s_b)

            heapq.heappush(res, -diff)

        return -res[0]