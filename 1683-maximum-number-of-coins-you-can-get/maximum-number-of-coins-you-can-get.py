class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        left=1
        right= len(piles)-1
        tot_coins=0
        while left<right:
            tot_coins +=piles[left]
            left+=2
            right-=1
        return tot_coins

        