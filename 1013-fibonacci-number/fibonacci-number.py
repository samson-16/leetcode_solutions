class Solution:
    def fib(self, n: int) -> int:

        memo = {0:0, 1:1}
        def helper(n):
           
            if n in memo:
                return memo[n]
            
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)

        