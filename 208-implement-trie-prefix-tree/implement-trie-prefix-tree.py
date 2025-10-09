class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[ord(c)-97] == None:
                cur.children[ord(c)-97] = TrieNode()
            cur = cur.children[ord(c)-97]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if cur.children[ord(c)-97] == None:
                return False
            cur = cur.children[ord(c)-97]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if cur.children[ord(c)-97] == None:
                return False
            cur = cur.children[ord(c)-97]
        return True
            

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)