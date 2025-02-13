class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        k= len(s1)
        l=0
        win= s2[l:k]
        
        w_counter = Counter(win)
        if w_counter == s1_counter:
            return True
        for r in range(k,len(s2)):
            l+=1
            win= s2[l:r+1]
            w_counter = Counter(win)
            
            if w_counter == s1_counter:
                return True
        return False



           

            




        