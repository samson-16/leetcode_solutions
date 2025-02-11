class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ht = defaultdict(int)
        # seen = set()
        count =0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                prod = nums[i]*nums[j]
                # if prod in seen: 
                ht[prod]+=1
        for value in ht.values():
            count+=( 2*value)*(2*(value-1))
        return count
