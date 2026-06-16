class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP array contains the number of coins needed to reach amount 'a'
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0]=0

        # dp array contains no. of coins [0,0,0,0,0,0], idx is amount

        for amt in range(1,amount+1):
            for coin in coins:
                if amt-coin >= 0:
                    dp[amt] = min(dp[amt], 1+dp[amt-coin])

        return dp[amount] if dp[amount] != float('inf') else -1

        """
        amt = 1
        coins => 1,5,10
        dp[1]=min(dp[1], 1+dp[amt-1]) = 1

        amt=2
        dp[2]=min(dp[2], 1 + dp[amt-1]) = 2

        coin = 1
        dp[5]=min(dp[5], 1+dp[amt-1]) = 5

        coin = 5
        dp[5] min(dp[5], 5)

        """

        