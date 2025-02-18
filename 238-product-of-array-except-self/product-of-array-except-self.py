class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right= [1] *n
        for l in range(1,n):
            left[l] = left[l-1] * nums[l-1]
        for r in range(n-2,-1,-1):
            right[r] = right[r+1] * nums[r+1]
        
        ans =[]
        for i in range(n):
            ans.append(left[i]*right[i])
        return ans

        
        