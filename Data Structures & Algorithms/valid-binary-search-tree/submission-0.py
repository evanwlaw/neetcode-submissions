# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BST. A node is valid if it's within the range bounds of ancestors
        TC and SC: O(n)

        """
        queue = [(root, float('-inf'), float('inf'))]
        
        while queue:
            node, left_bound, right_bound = queue.pop()
            if not left_bound < node.val < right_bound:
                return False
            if node.left:
                queue.append((node.left, left_bound, node.val))

            if node.right:
                queue.append((node.right, node.val, right_bound))

        return True