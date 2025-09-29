class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
            
        dp=[[0] * len(s) for _ in range(n)]

        for i in range(n):
            dp[i][i] =1
        
        for d in range(1, n):
            for l in range(n-d):
                r=l+d
                if s[l]==s[r]:
                    dp[l][r]=dp[l+1][r-1]+2
                else:
                    dp[l][r]= max(dp[l+1][r], dp[l][r-1])
        return dp[0][n-1]
            
