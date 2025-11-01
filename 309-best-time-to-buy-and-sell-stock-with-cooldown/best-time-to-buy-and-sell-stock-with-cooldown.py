class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dp(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in memo:
                return memo[(i,state)]
            
            if state == "hold":
                memo[(i,state)] = max(dp(i+2,'free') + prices[i],dp(i+1, "hold") )
            else:
                memo[(i,state)] = max(dp(i+1, 'hold') - prices[i], dp(i+1, 'free'))
            
            return memo[(i,state)]
        return dp(0,"free")