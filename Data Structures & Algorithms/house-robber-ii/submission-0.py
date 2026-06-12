class Solution:
    def findMax(self, arr):
        n=len(arr)
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])

        dp = [0]*n

        dp[0]=arr[0]
        dp[1]=max(dp[0], arr[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], arr[i]+dp[i-2])
        
        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        max1 = self.findMax(nums[1:])
        max2 = self.findMax(nums[:-1])

        return max(max1, max2)