class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left, right = 1, len(skill)-2
        team = skill[0]+skill[-1]
        chemistry= skill[0]*skill[-1]
        flag = True
        while left < right:
            cur_sum = skill[left] +skill[right]
            if cur_sum != team:
                flag  = False
                break
            else:
                chemistry += skill[left] * skill[right]
            left+=1
            right-=1
                
        return chemistry if flag else -1