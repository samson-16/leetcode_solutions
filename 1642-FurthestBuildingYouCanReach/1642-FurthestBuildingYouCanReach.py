# Last updated: 4/30/2025, 5:39:31 PM
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        i = 0
        
        while i < len(heights) - 1:
            if heights[i] < heights[i + 1]:
                heappush(min_heap, heights[i + 1] - heights[i])
            if len(min_heap) > ladders:
                  
                bricks -= heappop(min_heap)
                if bricks < 0:
                    return i
        
                
            i += 1
        return i