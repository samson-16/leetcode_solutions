class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        ans =[]
        rows  = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                hm[i+j].append(mat[i][j])

        
        for key,val in hm.items():
           
            if key%2!=0:
                ans.extend(val)
            else:
                ans.extend(val[::-1])
        return ans
        


    