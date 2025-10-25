class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v, t))
        print(graph)

        times = {node: float("inf") for node in range(1, n+1)}
        times[k] = 0
        processed = set()

        heap = [(0, k)]

        while heap:
            cur_time , cur_node = heappop(heap)
            if cur_node in processed:
                continue
            processed.add(cur_node)
            for child , time in graph[cur_node]:
                expected_time = time + cur_time
                if expected_time < times[child]:
                    times[child] = expected_time
                    heappush(heap, (expected_time, child))
       
        
        return -1 if inf in times.values() else max(times.values())