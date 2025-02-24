class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left, right = 0, total_sum
        result = []

        for i, n in enumerate(nums):
            right -= n
            result.append(n * i - left + right - n * (len(nums) - i - 1))
            left += n

        return result
        