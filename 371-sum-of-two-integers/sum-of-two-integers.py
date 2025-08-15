class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a =a&mask
        b = b & mask

        while b:
            carry = (a & b) <<1
            a = (a^ b) & mask
            b = carry  & mask
        return a if a <=MAX_INT else ~(a^mask)


