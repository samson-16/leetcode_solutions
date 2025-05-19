# Last updated: 5/19/2025, 6:23:51 PM
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        nums1_xor,  nums2_xor=0,0
        if len(nums1)%2!=0:
            for num in nums2:
                nums2_xor^=num
        
        if len(nums2)%2!=0:
            for num in nums1:
                nums1_xor^=num
       
        return nums1_xor ^ nums2_xor
            
