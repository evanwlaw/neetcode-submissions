# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            9   9
        8   9   7
        9   9   6

        need to start from right side

        make two lists and pop from back
        """

        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        prev = None
        carry = 0
        while s1 or s2 or carry:
            s1Val = s1.pop() if s1 else 0
            s2Val = s2.pop() if s2 else 0

            sumVal = s1Val + s2Val + carry
            carry = sumVal // 10
            newNode = ListNode(sumVal % 10) # single digit

            newNode.next = prev
            prev = newNode

        return prev

            


