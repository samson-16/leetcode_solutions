class Solution:
    def canCross(self, stones: List[int]) -> bool:
        seen = set(stones)
        @cache
        def dp(stone, k):

            if stone == stones[-1]:
                return True

            for step in [k-1, k, k+1]:
                if step>0 and stone + step in seen:
                    if dp(stone + step, step):
                        return True
           
           
            return False
        if stones[1] !=1:
            return False
        return dp(1, 1)
