class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_dict ={}
        nums_sorted = sorted(nums)

        for i, num in enumerate(nums_sorted):
            if num not in nums_dict:
                nums_dict[num]= i
        return [nums_dict[num] for num in nums]
        