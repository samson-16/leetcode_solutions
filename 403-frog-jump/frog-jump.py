class Solution:
    def canCross(self, stones: List[int]) -> bool:
        seen = set(stones)
        @cache
        def dp(stone, k):

            if stone == stones[-1]:
                return True
            if stone >  stones[-1]:
                return False

           
            if k>0 and stone + k in seen:
                if dp(stone+k, k):
                    return True
            if k> 0 and stone + k+1 in seen:
                if dp(stone + k+1, k+1):
                    return True
            if k>0 and stone + k-1 in seen:
                if dp(stone + k -1, k-1):
                    return True
            return False
        if stones[1] !=1:
            return False
        return dp(1, 1)
