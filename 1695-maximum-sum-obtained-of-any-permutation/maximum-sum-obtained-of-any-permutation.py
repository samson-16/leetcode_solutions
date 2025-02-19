class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        linesweep = [0]  * (len(nums)+1)

        for s,e in requests:
            linesweep[s]+=1
            linesweep[e+1]-=1
        for i in range(len(nums)):
            linesweep[i+1] += linesweep[i] 
       

        nums.sort(reverse=True)
        linesweep.sort(reverse=True)
        ans =0
        for i in range(len(nums)):
            ans+= linesweep[i] *nums[i] 
        return ans% (10**9 +7)

        