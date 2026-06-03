import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        ans=[]

        for x,y in points:
            dist = math.sqrt((x*x)+(y*y))
            res.append((dist, [x,y]))
        
        heapq.heapify(res)

        for i in range(k): 
            ans.append(heapq.heappop(res)[1])

        return ans
        
        