# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        cut in halves.

        reverse second half

        zip to first half
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # make slow node the start of the second LL 
        slow.next = None
        prev = None
        # print(second.val)

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2