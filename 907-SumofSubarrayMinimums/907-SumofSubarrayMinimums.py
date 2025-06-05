# Last updated: 6/5/2025, 11:20:00 AM
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ple =[]
        nle =[]
        n =  len(arr)
        pstack=[]
        for i in range(len(arr)):
            while pstack and arr[pstack[-1]]  > arr[i]:
                pstack.pop()
            if not pstack:
                ple.append(-1)
            else:ple.append(pstack[-1])
            pstack.append(i)
        nstack=[]
        for j in range(n-1,-1,-1):
            while nstack and arr[nstack[-1]]  >= arr[j]:
                nstack.pop()
            if not nstack:
                nle.append(len(arr))
            else:nle.append(nstack[-1])
            nstack.append(j)

        nle.reverse()
        MOD = 10**9 + 7
        total =0
        for i in range(n):
            left = abs(i-ple[i])
            right = abs(nle[i]-i)
            total +=(arr[i]*left*right)
        return total % MOD
        
