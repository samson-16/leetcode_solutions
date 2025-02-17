class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        for char in word:
            freq[char]-=1
            if freq[char]==0:
                del freq[char]
            if len(set(freq.values()))==1:
                return True
            freq[char]+=1
        return False


            
        