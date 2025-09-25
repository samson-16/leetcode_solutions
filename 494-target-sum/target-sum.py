class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo ={}
        n = len(nums)
        def dp(i, cur):
            if i == n:
                return 1 if cur ==target else 0
            
            if (i, cur) in memo:
                return memo[(i, cur)]
            
            add = dp(i+1, cur + nums[i])
            substract = dp(i+1 , cur - nums[i])

            memo[(i,cur)] = add + substract
            return memo[(i,cur)]
        return dp(0,0)
        


