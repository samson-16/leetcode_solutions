class Solution:
    def tribonacci(self, n: int) -> int:
        ans =0
        @cache
        def dp(i):
            nonlocal ans
            if i==0:
                return 0
            if i==1:
                return 1
            if i==2:
                return 1
            
            return dp(i-1)+dp(i-2)+dp(i-3)
            # return ans

        return dp(n)


        
