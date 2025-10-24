class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
      
        def prime_sieve(n):
            is_prime = [True for _ in range(n+1)]
            is_prime[0] = is_prime[1] = False
            
            i = 2
            while i*i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        
                        j += i
                i += 1
            return is_prime
        
        res = prime_sieve(n)
        count = 0
        for i in range(n):
            if res[i] == True:
                count += 1
        return count
        