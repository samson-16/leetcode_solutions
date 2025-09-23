class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo ={}
        n = len(nums)
        total = sum(nums)
        if total % 2 ==1:
            return False
        half = total//2

        def dp(end, weight):

            if weight > half:
                return False
            if weight == half:
                return True
        
            if end < 0:
                return False
            if (end, weight) in memo:
                return memo[(end, weight)]
            # cur = weight + nums[end]
            # take  = dp(end-1, cur)

            # notake = dp(end-1,weight)

            memo[(end, weight)] = (dp(end-1, weight + nums[end]) or dp(end-1, weight))

            return memo[(end, weight)]
        return dp(n-1, 0)

