class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        k= len(s1)
        l=0
        win= list(s2[l:k])
        
        w_counter = Counter(win)
        if w_counter == s1_counter:
            return True
        for r in range(k,len(s2)):
            win.remove(s2[l])
            w_counter[s2[l]] -=1
            if w_counter ==0:
                del w_counter[s2[l]]
            l+=1
            win.append(s2[r])
    
            w_counter = Counter(win)
            
            if w_counter == s1_counter:
                return True
        return False



           

            




        