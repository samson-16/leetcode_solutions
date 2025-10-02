class Solution:
    def climbStairs(self, n: int) -> int:
       
        memo={}
        def dp(stair):
            
            if stair+2==n:
                return 2
            if stair +1==n:
                return 1
            if stair in memo:
                return memo[stair]
            memo[stair]=dp(stair+2) + dp(stair+1)
            return memo[stair]
        return dp(0)
    