"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        2 ptrs go upwards until meet
        """

        pt1, pt2 = p, q

        while pt1 != pt2:
            pt1 = pt1.parent if pt1 else q
            pt2 = pt2.parent if pt2 else p
        return pt1