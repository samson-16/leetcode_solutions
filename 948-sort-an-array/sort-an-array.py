class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        large = max(nums)
        small = abs(min(nums))

        count = [0] *(large + small+1)
        target =0
        for i in nums:
            count[i+small] +=1
        for index, val in enumerate(count):

            for _ in range(val):
                nums[target] = index-small
                target +=1
        return nums
