# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Restate + example: return a linkedlist that's reordered.
        order is idx by 0, end-1, 1, end-2, 2, end-3....

        we can break the input linked list into 2 halves -> first and second
        Then "zip" the two linked lists alternating
        
        1. Break linked list into 2 half lists
            - use slow and fast ptrs to get halves
        
        2. Second half list needs to be in reverse order -> reverse

        3. alternate adding nodes from first and second halves


        Trace:
        Input: head = [2,4,6,8,10]
        Output: [2,10,4,8,6]

        org: 2   4   6   8   10
        first: 2    4
        second: 10  8   6

        zip to dummy node with first then second:
            2   10  4   8   6

        There might be a case where one of halves might be longer.
        So in the "zip", we zip while both have nodes.

        Then attach the rest 
        """

        # 1. break linked list into 2 halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second = slow.next # slow node is the start of second LL
        slow.next = None 
        prev = None
        # 2. Second half list needs to be in reverse order -> reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head
        # 3. Zip halves
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
