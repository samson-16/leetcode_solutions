class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left, right = 0, len(skill)-1
        team = skill[0]+skill[-1]
        chemistry= 0
        flag = True
        while left < right:
            cur_sum = skill[left] +skill[right]
            if cur_sum != team:
               return -1
            else:
                chemistry += skill[left] * skill[right]
            left+=1
            right-=1
                
        return chemistry