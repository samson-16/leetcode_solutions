# Last updated: 5/14/2025, 10:37:46 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            ans =0
            for num in nums:
                ans^=num
            return ans