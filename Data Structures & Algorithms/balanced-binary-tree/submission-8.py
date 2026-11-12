# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        if leftheight - rightheight > 1
        """

        def dfs(node):
            if not node:
                return [0, True]

            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left[0] - right[0]) <= 1 and left[1] and right[1]:
                return [max(left[0], right[0]) + 1, True]

            return [max(left[0], right[0]) + 1, False]
        

        return dfs(root)[1]