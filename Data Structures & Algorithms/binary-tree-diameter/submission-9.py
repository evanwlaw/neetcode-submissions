# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        len of longest path -> path with the most edges

        dfs to get edges on left and right
        return num of edges
        """
        output = 0

        def dfs(node):
            nonlocal output
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            output = max(output, left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return output