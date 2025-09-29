class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        memo ={}

        def dp(r):
            if r ==0:
                return 0
            if r in memo:
                return memo[r]
            memo[r] = inf
            for coin in coins:
                if r >= coin:
                    memo[r] = min(memo[r], dp(r-coin)+1)
            return memo[r]
        ans = dp(amount)
        return -1 if ans ==float("inf") else ans
        # min_count = defaultdict(lambda: float("inf"))
        
        # def dp(end, a):
        #     nonlocal min_count
           
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return float("inf")
        #     if end == n:
        #         return float("inf")
        #     for i in range(n):
        #         take = 1+  dp(end+1, a + coins[i])
        #         notake = dp(end+1, a)
        #         min_count[(end,a)] = min(take, notake, min_count[(end, a)])
        #     return min_count[(end, a)]
        # dp(0,0)
        # return -1 if min_count[(0,0)] == float("inf") else min_count[(0,0)]

