# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        return sum of two nums as a linked list
        and the digits are in reverse order

        Input: l1 = [1,2,3], l2 = [4,5,6]
        Output: [5,7,9]
        Explanation: 321 + 654 = 975.

            1   1
 l1     8   2   1
 l2     7   9   9
        5   2   1   1 -> 1120


        """
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            l1n = l1.val if l1 else 0
            l2n = l2.val if l2 else 0
            
            sumDigit = l1n + l2n + carry # what if it's 15?

            if carry > 0:
                carry -= 0
                
            carry = sumDigit // 10 # 1
            sumDigit %= 10 # if 15, 5

            # create new node
            curr.next = ListNode(sumDigit)

            # update ptrs
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
            
        return dummy.next

