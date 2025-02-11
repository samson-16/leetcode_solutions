class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ht = defaultdict(int)
       
        count =0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                prod = nums[i]*nums[j]
                ht[prod]+=1
        for pairs in ht.values():
            #count+=( 2*pairs) *1*(2*(pairs-1))*1
            count += (2 * pairs) * (2 * (pairs-1))
        return count