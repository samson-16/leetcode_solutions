# Last updated: 5/14/2025, 12:27:28 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n =len(nums)
        ans =[]
        for  i in range(1<<n):
            temp= []
            for j in range(32):
                if i & (1<<j) !=0:
                    temp.append(nums[j])
            ans.append(temp)
        return ans
