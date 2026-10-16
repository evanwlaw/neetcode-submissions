"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        cant necessarily copy ranndom nodes to the new random nodes if we havent seen them yet
        """
        if not head:
            return None
        hashMap = {} # oldNode : NewNode

        curr = head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            hashMap[curr].random = hashMap[curr.random] if curr.random else None
            hashMap[curr].next = hashMap[curr.next] if curr.next else None
            curr = curr.next
        return hashMap[head]