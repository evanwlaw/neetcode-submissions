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
        two pass.
        use a hashmap to get hte new copy
        """

        nodeMap = {} # node : newNode

        curr = head
        while curr:
            # create node
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            newNode = nodeMap[curr]
            newNode.random = nodeMap[curr.random] if curr.random else None
            newNode.next = nodeMap[curr.next] if curr.next else None
            curr = curr.next
                
        return nodeMap[head] if head else None

