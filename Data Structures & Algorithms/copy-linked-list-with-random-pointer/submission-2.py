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
        3:null      7:3     4:0     5:2
        """
        if not head: return None

        copy_dict = {}

        curr = head

        while curr:
            copy_dict[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            new_node = copy_dict[curr]
            new_node.next = copy_dict[curr.next] if curr.next else None
            new_node.random = copy_dict[curr.random] if curr.random else None
            curr = curr.next
        
        return copy_dict[head]
