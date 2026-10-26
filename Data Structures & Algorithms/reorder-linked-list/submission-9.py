# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Input: head = [2,4,6,8]
        Output: [2,8,4,6]

        so seems we interchange with back half of linkedlist

        1. split in half
        2. reverse second half
        3. zip/interchange first half with second reversed half

        no need to return anything
        """
        # split in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #   2   4   6   8
    #          s
    #                   f
        # slow is one node before split/start of second
        second = slow.next
        slow.next = None

        # reverse
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first = head
        second = prev

        # zip
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

