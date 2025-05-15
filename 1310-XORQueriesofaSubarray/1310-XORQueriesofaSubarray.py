# Last updated: 5/15/2025, 7:10:59 PM
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref = [0]*n
        pref[0] = arr[0]
        ans =[]
        for i in range(1,n):
            pref[i] = pref[i-1]^arr[i]
    
        for a,b in queries:
            if a:
                ans.append(pref[b]^pref[a-1])
            else:
                ans.append(pref[b])
        return ans
6