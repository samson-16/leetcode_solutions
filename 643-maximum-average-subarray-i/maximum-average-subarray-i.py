class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average=0
        if len(nums)==1:
            return float(nums[0])
        w=nums[0:k]
        range_sum=sum(w)
        max_sum =range_sum
        # average= 0
        l=0
        for r in range(k,len(nums)):
            range_sum=range_sum-nums[l]+nums[r]
            max_sum = max(range_sum,max_sum)
            l+=1
        return max_sum/k
