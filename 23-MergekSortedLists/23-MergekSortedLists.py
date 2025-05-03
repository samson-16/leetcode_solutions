# Last updated: 5/3/2025, 6:14:19 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, (lists[i].val,i,lists[i]))
            # list[i] = list[i].next
        
        dum_node = ListNode()
        
        ptr = dum_node
        while min_heap:
            val ,i, node = heappop(min_heap)
            ptr.next = node
            if node.next:
                heappush(min_heap,(node.next.val,i, node.next))
            ptr = ptr.next
        return dum_node.next