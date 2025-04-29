# Last updated: 4/29/2025, 6:04:36 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_heap = [(0, k)]  # (time, node)
        visited = set()
        dist = {}

        while min_heap:
            time, node = heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            dist[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heappush(min_heap, (time + weight, neighbor))

        return max(dist.values()) if len(dist) == n else -1