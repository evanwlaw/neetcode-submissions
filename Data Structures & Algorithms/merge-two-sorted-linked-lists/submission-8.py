# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        dummy = ListNode(0)
        
        curr = dummy
        while list1 and list2:
            # if list1 smaller
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            
            # if list 2 smaller
            else:
                curr.next = list2
                list2 = list2.next
            # update ptrs
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next
