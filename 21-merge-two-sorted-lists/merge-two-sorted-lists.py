# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1= list1.next
            elif list1.val > list2.val:
                temp.next = list2
                temp = temp.next
                list2= list2.next
            else:
                temp.next = list1
                temp = temp.next
                list1= list1.next
                temp.next = list2
                temp = temp.next
                list2= list2.next
        if list1:
            temp.next = list1
        if list2:
            temp.next=list2
        
        return dummy.next


            



       
    
               