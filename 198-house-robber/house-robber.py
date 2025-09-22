class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        # n = len(nums)
        def helper(i):
            if i >= len(nums):
                return 0
            rob, skip =0,0
            if i not in memo:
                rob+= (nums[i]+helper(i+2))
                skip+=helper(i+1)
                memo[i] = max(rob, skip)
            return memo[i]
        return helper(0)


