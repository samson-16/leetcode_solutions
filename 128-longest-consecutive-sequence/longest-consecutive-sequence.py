class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
       
        max_count =0
        for num in seen:
            count =1
            if num - 1 not in seen:
                cur = num
                while cur +1 in seen:
                    cur +=1
                    count +=1
                
            max_count = max(count,max_count)
        return max_count
                    


       

