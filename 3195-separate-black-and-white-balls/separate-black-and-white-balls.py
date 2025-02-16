class Solution:
    def minimumSteps(self, s: str) -> int:
        z_count = 0
        swaps = 0

        for c in s:
            if c == '1':
                z_count += 1  
            else:
                swaps += z_count  

        return swaps
