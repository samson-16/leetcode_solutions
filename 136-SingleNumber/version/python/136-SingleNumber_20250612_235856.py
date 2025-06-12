# Last updated: 6/12/2025, 11:58:56 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans =0
        for num in nums:
            ans^=num
        return ans
