class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp =[0] * (n+1)

        for i in range(n-1, -1,-1):
            point, power = questions[i]
            
            solve = point + (dp[i+power+1] if (i + power + 1 ) <= n else 0)
            skip = dp[i+1]
            dp[i] = max(skip, solve)
        return dp[0]