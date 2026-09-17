# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input: l1 = [1,2,3], l2 = [4,5,6]
        Output: [5,7,9]
        Explanation: 321 + 654 = 975.

        123
        956
        089
        
        start from 1st nodes of each.

        No gurantee that len(l1) == len(l2)

        So in the adding of l1 and l2, we want to keep adding while both are non empty + if a carry exists



        """

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = l1_val + l2_val + carry

            # get carry
            carry = sum_val // 10 # if 15, then 1. if 5, then 0
            
            # get ones place
            ones_place = sum_val % 10 # if sum_val is 15 
            curr.next = ListNode(ones_place)
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next
