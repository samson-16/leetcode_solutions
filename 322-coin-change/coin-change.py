class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [inf] * (amount+1)

        dp[0] =0

        for rem in range(amount+ 1):
            for coin in coins:
                if rem >= coin:
                    dp[rem]= min(dp[rem], dp[rem-coin]+1)
        ans = dp[amount]

        return -1 if ans == inf else ans