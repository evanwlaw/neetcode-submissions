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

        need to start from right side -> put nodes into 2 lists

        sum them together
            add digits from the back
        """

        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        # s1 = [9,9], s2 = [9,9,6] -> pop from back
        carry = 0

        prev = None
        while s1 or s2 or carry:
            s1Val = s1.pop() if s1 else 0
            s2Val = s2.pop() if s2 else 0

            addSum = s1Val + s2Val + carry
            carry = addSum // 10 # 15 -> 1 carry
            digit = addSum % 10 # 15 -> 5 digit

            # add digit to end of linkedlist
            newNode = ListNode(digit)
            # prev = newNode
            # prev = prev.next

            # reviewed code for the linkedlist part
            newNode.next = prev
            prev = newNode
            
        return prev