class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] * n
     
        for i in range(1,n):
            max_val =0
            for k in range(i):
               
                if nums[k] < nums[i]:
                    max_val = max(max_val,arr[k])
            
            arr[i]= max_val+1
        
      
        return max(arr)
            
            
            

        