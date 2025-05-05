# Last updated: 5/5/2025, 10:45:51 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        def inbound(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        def dfs(i,j):
            if not inbound(i, j) or grid[i][j]==0 or (i, j) in visit:
                return 0
            visit.add((i,j))
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area
            
        max_area =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visit and grid[i][j]==1:
                    max_area = max(dfs(i,j), max_area)
        return max_area