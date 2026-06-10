class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)

        def backtrack(arr, idx):
            if idx == n:
                res.append(arr[:])
                return
            
            # take
            arr.append(nums[idx])
            backtrack(arr, idx+1)
            # not take
            arr.pop()
            backtrack(arr, idx+1)

        backtrack([],0)
        return res