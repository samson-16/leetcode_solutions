# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #N
        n=0
        cur = head
        while cur:
            cur = cur.next
            n +=1
        # print(n)
        move = n//2 -1
        print(move)
        f = head
        s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        prev = None
        while s:
            nxt = s.next
            s.next = prev
            prev = s
            s = nxt  
        left , right  = head, prev
        max_sum =0
        while right:
            cur_sum = left.val +right.val
            max_sum = max(max_sum, cur_sum)
            left = left.next
            right = right.next
        return max_sum




        
        