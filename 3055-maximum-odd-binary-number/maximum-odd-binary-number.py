class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
    
        if len(s)==1:
            return s
        ans = ["0"]*len(s)
        count = Counter(s)
        ans[-1]='1'
        count['1']-=1
        for i in range(len(s)):
            if count["1"] >0:
                ans[i]="1"
                count['1']-=1
        return "".join(ans)
        