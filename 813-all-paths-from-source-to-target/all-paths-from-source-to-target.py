class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        stack  = [(0, [0])]
        ans = []

        while stack:
            nd, pth = stack.pop()
            if nd == N - 1:
                ans.append(pth)
                continue

            for ne in graph[nd]:
                stack.append((ne, pth + [ne]))
        
        return ans
            
        