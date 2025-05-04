# Last updated: 5/4/2025, 5:54:18 PM
from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)  # Add original index

        tasks.sort()  # Sort by enqueue time

        res = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or min_heap:
            # If no tasks are available in heap, jump time forward
            if not min_heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Add all available tasks up to current time
            while i < n and tasks[i][0] <= time:
                heappush(min_heap, (tasks[i][1], tasks[i][2]))  # (processingTime, index)
                i += 1

            if min_heap:
                pt, idx = heappop(min_heap)
                time += pt
                res.append(idx)

        return res
