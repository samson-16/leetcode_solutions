class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [inf] * n
        dp[0]=0
        
        for i in range(m):
            for j in range(n):
                if j ==0:
                    dp[j] += grid[i][0]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        
        return dp[-1]
            


                


