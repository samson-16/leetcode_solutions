# Last updated: 5/5/2025, 1:57:05 PM
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
     
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
        return True  
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFind(26)
        for i in range(n):
            if equations[i][1] =="=":
                uf.union(ord(equations[i][0])-97,  ord(equations[i][3])-97)
        for i in range(n):
            if equations[i][1] =="!":
                if uf.connected(ord(equations[i][0])-97,  ord(equations[i][3])-97):
                    return False
        return True

        