class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp=heights[:]
        exp.sort()
        count=0
        for i in range(len(exp)):
            if heights[i]!=exp[i]:
                count+=1

        return count