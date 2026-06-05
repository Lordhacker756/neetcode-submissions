class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]

        def backtrack(res, i):
            if sum(res) == target:
                result.append(res[:])
                return

            if i == len(nums) or sum(res) > target:
                return

            # don't take the element
            backtrack(res, i+1)

            # take the element
            res.append(nums[i])
            backtrack(res, i)
            res.pop()

        
        backtrack([], 0)

        return result