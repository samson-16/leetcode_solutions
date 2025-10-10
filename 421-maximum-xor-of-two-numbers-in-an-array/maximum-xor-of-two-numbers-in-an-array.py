class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None
class Solution:
  
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        # building the trie
        for num in nums:
            node = root
            for i in range(31, -1,-1):
                bit = num & (1 << i)
                bit = 1 if bit else 0

                if bit and not node.one:
                    node.one = TrieNode()
                    node = node.one
                    continue
                elif not bit and not node.zero:
                    node.zero = TrieNode()
                    node = node.zero
                    continue
                
                node = node.one if bit else node.zero

        #traversing the trie using the complements for every number to find the maximum xor value
        maxi =0
        for num in nums:
            node = root
            cur_num =0
            for i in range(31, -1,-1):
                bit = num & (1 << i)
                bit = 0 if bit else 1

                if bit and node.one:
                    # print(1<<i)
                    cur_num += (1 << i)
                    node = node.one
                elif bit and node.zero:
                    node = node.zero

                elif not bit and node.zero:
                    cur_num += (1 << i)
                    node = node.zero
                elif not bit and node.one:
                    node = node.one
     
            maxi = max(maxi,  cur_num)
        return maxi
                

                    





        
        




        