class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [[intervals[0][0], intervals[0][1]]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= ans[-1][1]:
                if end > ans[-1][1]:
                    ans[-1][1] = end
            else:
                ans.append([start, end])
                
        return ans
