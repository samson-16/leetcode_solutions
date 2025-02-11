class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * (max(nums)+1)

        for i in nums:
            count[i] += 1
        target =0
        for i , val in enumerate(count):
            # for j in range(i+1):
            for j in range(val):
                nums[target] = i

                target+=1
        return nums
        



        