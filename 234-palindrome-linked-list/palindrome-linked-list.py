# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast =fast.next.next
            slow = slow.next
        prev = None
        while slow:
            next_node =  slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        # return prev
        left , right = head, prev
        while right:
            if right.val!= left.val:
                return False
            left = left.next
            right = right.next
        return True     
            




                   