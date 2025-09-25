class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(wordDict)
        memo ={}    
        def dp( id):
            
            # if len(string) > len(s):
            #     return False
            # if end > n:
            #     return False
            if id == len(s):
                return True
            if id in memo:
                return memo[id]
            for i in range(len(wordDict)):
                m = len(wordDict[i])
                if s[id:id+m] == wordDict[i]:
                    
                    take = dp( id + m)
                    memo[id] = take
                    if take:
                        return True
                
                # notake = dp( string)
                # print(string)
            memo[id] = False
            return memo[id]
            
        return dp(0)