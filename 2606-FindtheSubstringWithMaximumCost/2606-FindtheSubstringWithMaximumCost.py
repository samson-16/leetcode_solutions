# Last updated: 5/30/2025, 6:14:06 PM
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_cost = {chars[i]: vals[i] for i in range(len(chars))}

        
        cost_array = []
        for c in s:
            if c in char_cost:
                cost_array.append(char_cost[c])
            else:
                cost_array.append(ord(c) - ord('a') + 1)

        # Step 3: Apply Kadane's Algorithm
        max_sum = 0
        current_sum = 0
        for cost in cost_array:
            current_sum = max(cost, current_sum + cost)
            max_sum = max(max_sum, current_sum)

        return max_sum
