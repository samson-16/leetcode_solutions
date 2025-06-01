# Last updated: 6/1/2025, 7:34:41 PM

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        for right in range(len(nums)):
    
            if nums[right] == 0:
                k -= 1
            
            while k<0 and left<len(nums):
                if nums[left] == 0:
                    k +=1        
                left += 1
            ans = max(ans, right - left + 1)
            
               
        return ans