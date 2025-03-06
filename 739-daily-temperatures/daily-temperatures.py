class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n= len(temperatures)
        ans=[0]* n
        for i in range(len(temperatures)):
            while stack and stack[-1][0] <temperatures[i]:
                ans[stack[-1][1]]= i-stack[-1][1]
                stack.pop()
            else:
                stack.append([temperatures[i],i])
        return ans 
        

        