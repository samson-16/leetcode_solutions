class Solution:
    def validPalindrome(self, s: str) -> bool:
        c =0
        count =Counter(s)
        l=0
        r=len(s)-1
        def ispalindrome(substring):
            return substring == substring[::-1]
        
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                
            else:
                if ispalindrome(s[l:r]) or ispalindrome(s[l+1:r+1]):
                    return True
                else:
                    return False
        return True
        
                
                
       