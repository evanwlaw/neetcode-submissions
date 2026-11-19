# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def lltoList(node, listVal):
            while node:
                listVal.append(node.val)
                node = node.next
            return listVal
        
        list1, list2 = lltoList(l1, []), lltoList(l2, [])
        carry = 0
        head = None
        while list1 or list2 or carry:
            l1Val = list1.pop() if list1 else 0
            l2Val = list2.pop() if list2 else 0

            sumVal = l1Val + l2Val + carry
            carry = sumVal // 10 # 15 //10 = 10, 9//10 = 0
            newNode = ListNode(sumVal % 10) # 15 % 10 = 5

            newNode.next = head
            head = newNode
        return head




