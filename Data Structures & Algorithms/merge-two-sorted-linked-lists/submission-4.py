# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1: 1   2   4
            *

        l2: 1   3   5
                *
        
        d   
            c   
            1
        """
        
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # edge case where either list1 or list2 still have
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next
        


        