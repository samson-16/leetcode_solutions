class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
       
        max_count =0
        for num in seen:
            count =1
            if num - 1 not in seen:
                for i in range(1, len(nums)+1):
                    if num + i in seen:
                        count +=1
                    else:
                        break
                # print(count)
            max_count = max(count,max_count)
        return max_count
                    


       

