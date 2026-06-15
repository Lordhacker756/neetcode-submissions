class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #initialize answer with the first item
        ans=nums[0]
        leftPdt=1
        rightPdt=1
        n=len(nums)

        for i in range(n):
            leftPdt = leftPdt if leftPdt != 0 else 1
            rightPdt = rightPdt if rightPdt != 0 else 1

            leftPdt*=nums[i]
            rightPdt*=nums[n-i-1]

            ans = max(ans, leftPdt, rightPdt)

        return ans