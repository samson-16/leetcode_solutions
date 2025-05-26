# Last updated: 5/26/2025, 7:13:40 PM
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(a, b):
            diff = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            return (len(diff) == 2 and 
                    a[diff[0]] == b[diff[1]] and 
                    a[diff[1]] == b[diff[0]]) or len(diff) == 0

        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)

        return len(set(uf.find(i) for i in range(n)))
