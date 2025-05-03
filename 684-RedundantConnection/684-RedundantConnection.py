# Last updated: 5/3/2025, 1:42:09 AM
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [i for i in range(n)]
        self.rank = [0] * n
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
        # while  x !=self.root[x]:
        #     self.root[x] = self.find(self.root[x])
        # return self.root[x]
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
            
          
    # def connected(self, x, y):
    #     if self.find(x) == self.find(y):

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n =  len(edges)
        unionfind = UnionFind(n)
        for n1, n2 in edges:
            if not unionfind.union(n1-1,n2-1):
                return [n1, n2]
            