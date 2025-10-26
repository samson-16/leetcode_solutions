class TrieNode:
    def __init__(self):
        self.children = {}   # Map from character -> TrieNode
        self.is_end = False  # Marks the end of a word

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

    def findRoot(self, word):
        node = self.root
        prefix = ""
        for ch in word:
            if ch not in node.children:
                return word
            node = node.children[ch]
            prefix += ch
            if node.is_end:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split(" ")
       
        for i in range(len(words)):
            words[i] = trie.findRoot(words[i])
        
        return " ".join(words)
        
        
        


        
        