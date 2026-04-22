# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        need to reverse kth. if less than kth, then leave as is

        1   2   3   4   5
    gp          k
                    gn
        3   2   1   4   5
        k           gn
                    pr
                gp

        func to get kth node -> if < k, break
        reverse up to kth -> until curr == gn
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next


    def getKth(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node