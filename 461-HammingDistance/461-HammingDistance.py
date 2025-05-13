# Last updated: 5/13/2025, 7:14:47 PM
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
        