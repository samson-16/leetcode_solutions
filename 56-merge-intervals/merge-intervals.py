class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        ans = [[intervals[0][0], intervals[0][1]]]
        
        prev = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= ans[prev][1]:

                if end > ans[prev][1]:
                    ans[prev][1] = end

            else:
                ans.append([start, end])
                prev +=1
        

        return ans