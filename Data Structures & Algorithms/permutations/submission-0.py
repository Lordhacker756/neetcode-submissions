class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(res):

            if len(res) == len(nums):
                result.append(res[:]) #copy of result

            #choices
            for num in nums:
                #constraint
                if num in res:
                    continue

                #make choice
                res.append(num)
                #backtrack with this res
                backtrack(res)
                #undo the choice
                res.pop()

        backtrack([])

        return result