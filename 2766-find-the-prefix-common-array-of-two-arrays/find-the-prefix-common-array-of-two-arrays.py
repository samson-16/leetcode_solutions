class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count  = defaultdict(int)
        res =[]
        c =0
        for i in range(len(A)):
            
        
            count[A[i]] +=1
            if count[A[i]] ==2:
                c +=1
                    
            count[B[i]] +=1
            if count[B[i]] ==2:
                c +=1
                

            res.append(c)
        return res
            

            
