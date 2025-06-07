# Last updated: 6/7/2025, 8:38:49 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0  # since all nums are positive, no product can be < 1

        prod = 1
        result = 0
        left = 0

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            result += (right - left + 1)

        return result