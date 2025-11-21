class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        best =[0] * n
        best[start_node] = 1
        heap =[(-1, start_node)]

        while heap:
            neg_prob , node = heappop(heap)
            prob = -neg_prob

            if node == end_node:
                return prob
            
            for nei, p in graph[node]:
                newprob = prob * p
                if newprob > best[nei]:
                    best[nei] = newprob
                    heappush(heap, (-newprob, nei))
        return 0
