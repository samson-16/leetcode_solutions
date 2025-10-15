# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reverse = []
        
        cur  = head
        while cur:
            reverse.append(cur.val)
            cur =cur.next
        reverse_head = ListNode()
        temp = reverse_head
        for num in reverse[::-1]:
            node = ListNode(num)
            temp.next = node
            temp = temp.next
        return reverse_head.next