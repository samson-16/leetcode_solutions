# Last updated: 5/23/2025, 8:04:00 PM
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_dsu = DSU(n)
        bob_dsu = DSU(n)
        removed = 0

        # Type 3 edges first
        for t, u, v in edges:
            if t == 3:
                a = alice_dsu.union(u, v)
                b = bob_dsu.union(u, v)
                if not a and not b:
                    removed += 1

        # Type 1 (Alice)
        for t, u, v in edges:
            if t == 1:
                if not alice_dsu.union(u, v):
                    removed += 1

        # Type 2 (Bob)
        for t, u, v in edges:
            if t == 2:
                if not bob_dsu.union(u, v):
                    removed += 1

        if alice_dsu.components != 1 or bob_dsu.components != 1:
            return -1

        return removed
