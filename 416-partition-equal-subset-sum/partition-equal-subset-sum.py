class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        if tot%2!=0:
            return False
        
        half=tot//2
        n=len(nums)
        dp=[[False]*(half+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True

        for i in range(1, n+1):
            for w in range(1,half+1):
                if w < nums[i-1]:
                    dp[i][w]=dp[i-1][w]
                else:

                    dp[i][w] = dp[i-1][w-nums[i-1]] or dp[i-1][w]
        return dp[n][half]






