class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(res, start):
            if sum(res) == target:
                result.append(res[:])
                return

            if sum(res) > target or start == n:
                return

            for i in range(start, n):
                res.append(nums[i])
                backtrack(res, i)
                res.pop()

            return result

        backtrack([], 0)

        return result