class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        if tot%2:
            return False
        
        half=tot//2
        n=len(nums)
        dp=set()
        dp.add(0)
        for i in range(n):
           
            next_dp = set()
            for t in dp:
                if (t+nums[i])==half:
                    return True
                next_dp.add(t+nums[i])
                next_dp.add(t)
            dp=next_dp
      
        return True if half in dp else False






