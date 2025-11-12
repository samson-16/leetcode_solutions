class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        longest = 0
        
        for x in arr:
            prev = x - difference
            dp[x] = dp[prev] + 1
            longest = max(longest, dp[x])
        return longest