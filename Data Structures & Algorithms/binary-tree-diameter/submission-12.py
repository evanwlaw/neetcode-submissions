# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        need to know if path via current node is largest
        and then pass upwards the longest side + 1
        """
        self.output = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.output = max(self.output, left + right)

            return 1 + max(left, right)
        dfs(root)
        return self.output