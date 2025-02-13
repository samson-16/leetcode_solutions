class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        min_gap= float("inf")
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            
            while left < right:
                cur_sum = nums[i]+nums[left]+nums[right]
                gap = abs(target-cur_sum)
                if gap<min_gap:
                    ans = cur_sum
                    min_gap = gap
                if cur_sum == target:
                    return ans
                elif cur_sum <target:
                    left+=1
                else:
                    right-=1

               
        return ans


                



        
