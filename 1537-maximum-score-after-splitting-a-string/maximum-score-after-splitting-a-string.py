class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        left=[0]*n
        right=[0]*n
        
        if s[0] =="0":
            left[0] = 1
        for i in range(1,n-1):
            if s[i]=="0":
                left[i]= left[i-1] + 1
            else:
                left[i]= left[i-1]
        if s[-1] =="1":
            right[-1]=1
        for r in range(n-2,0,-1):
            if s[r]  =="1":
                right[r] =right[r+1]+1
            else:
                right[r] = right[r+1]
        total =0
        print(left)
        print(right)
        for i in range(n-1):
            total = max(total, left[i]+right[i+1])
        return total

        

        