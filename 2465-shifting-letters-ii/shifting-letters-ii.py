class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        change = [0] * (n+1)
        ans = ''
        for st,e,d in shifts:
            if d ==0:
                change[st] -=1
                change[e+1] +=1
            else:
                change[st] +=1
                change[e+1] -=1
        for i in range(1,n+1):
            change[i]+=change[i-1]
        print(change)

        for i in range(n):
            ans  += chr((ord(s[i])-97+change[i])%26+97)
        return ans
