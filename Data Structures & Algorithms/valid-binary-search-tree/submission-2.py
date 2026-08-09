# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            2
        1       3


            

        """
        
        queue = deque() # (left_value, root, right_value)
        queue.append((float("-inf"), root, float("inf")))
        while queue:
            for i in range(len(queue)):
                left_value, node, right_value = queue.popleft()

                if not left_value < node.val < right_value:
                    return False

                if node.left:
                    queue.append((left_value, node.left, node.val))
                if node.right:
                    queue.append((node.val, node.right, right_value))
        return True