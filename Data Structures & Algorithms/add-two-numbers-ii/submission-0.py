# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        """
        carry = 0
        s1, s2 = [],[]
        dummy = None
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        while s1 or s2 or carry:
            l1Val = s1.pop() if s1 else 0
            l2Val = s2.pop() if s2 else 0

            # add the vals
            addVals = l1Val + l2Val + carry # what if 15?

            # reset carry
            carry = addVals // 10 # 15 // 10 = 1

            # new single digit node
            node = ListNode(addVals % 10) # 15 % 10 = 5
            node.next = dummy
            dummy = node            
        
        return dummy
""" 
use two stacks to process from right
        1
s1      9   9
s2  8   9   7
        6
"""



