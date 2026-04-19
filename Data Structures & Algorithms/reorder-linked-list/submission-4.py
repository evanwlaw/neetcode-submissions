# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        two ptrs -> increment fast to the end. cut list in two

        0   1   2   3   4   5   6
                    s
                                f
        s.next -> none
        f -> reverse 

        first
        0   1   2   3
        second
        4   5   6

        tmp1 -> first.next
        tmp2 -> second.next

        first.next -> second
        second.next -> tmp1

        first -> tmp1
        second -> tmp2

        0   4
        """
        if not head: return None
        

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev, slow.next = None, None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first = head
        second = prev
        
        while first and second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


            