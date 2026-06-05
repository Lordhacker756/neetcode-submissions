class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)

        def backtrack(res, start):
            if sum(res) == target:
                result.append(res[:])
                return

            if sum(res) > target:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                res.append(candidates[i])
                backtrack(res, i+1)
                res.pop()

        backtrack([], 0)
        return result
