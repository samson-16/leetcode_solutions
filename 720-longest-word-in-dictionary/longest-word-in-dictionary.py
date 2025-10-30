
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # trie = Trie()
        words.sort()
        word_set = set(words)
        print(word_set)
        ans = ""
        for word in words:
            flag = True
            for i in range(1,len(word)):
                if word[:i] not in word_set:
                    flag = False
                    break
            if flag:
                if len(word) > len(ans) or (ans and word < ans):
                    ans = word
        return ans            

        



