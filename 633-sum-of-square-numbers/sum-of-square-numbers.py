class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(sqrt(c))

        left =0

        while left <= right:
            prod= left**2 + right**2
            if prod == c:
                return True
            elif prod>c:
                right-=1
            else:
                left+=1
        return False
        