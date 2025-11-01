class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(end, state):
            if end == len(prices):
                return 0
            if (end, state) in memo:
                return memo[(end, state)]
            
            if state == "hold":
                memo[(end, state)] = max((dp(end+1,"free")+prices[end]), dp(end+1, "hold"))
            else:
                memo[(end, state)] = max((dp(end+1, "hold")-prices[end]-fee), (dp(end+1,'free')))
            return memo[(end, state)]
        return dp(0,"free")
