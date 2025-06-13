# Last updated: 6/13/2025, 11:24:46 PM
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
       

        graph = defaultdict(list)

        for a, b, score in roads:
            graph[a].append((b, score))
            graph[b].append((a, score))

        visited = set()
        min_score = float('inf')

        def dfs(node):
            nonlocal min_score
            visited.add(node)
            for neighbor, score in graph[node]:
                min_score = min(min_score, score)
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(1)
        return min_score