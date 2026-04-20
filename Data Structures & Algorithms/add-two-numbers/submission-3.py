# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

            1   1
        8   4   3
        4   5   6

        2   0   0   1

        carry = 0

        while l1 or l2 or carry
            if either l1.val or l2.val -> put 0

            sum = l1.val + l2.val + carry

            if carry > 0: carry -= 1
            
            if sum >= 10
                sum -> sum % 10       # get ones
                carry = 1
            
            node.val -> sum

        2   

        """
        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = l1_val + l2_val + carry

            if carry > 0: carry -= 1

            if sum_val >= 10:
                sum_val = sum_val % 10
                carry += 1
            
            curr.next = ListNode(sum_val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return dummy.next



        