class TrieNode:
    def __init__(self):
        self.children = {}   
        self.is_end = False  
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str):
        flag = True
        node = self.root
        for ch in word:
            node = node.children[ch]
            if not node.is_end:
                flag = False
                break
        return word if flag else ""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        for word in words:
            trie.insert(word)
        ans  = ''
        for word in words:
            temp = trie.search(word)
           
            if len(temp) > len(ans):
                ans =  temp
        return ans
        




        



