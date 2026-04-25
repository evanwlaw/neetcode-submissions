# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        left and right subtree len differs no more than 1
        
        dfs

        stack
        2   3   

        stack.pop()
        left = node.dfs(node.left)
        right = node.dfs(node.right)

        if abs(left-right) > 1:
            return False

        """
        self.balance = True
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.balance = False

            return 1 + max(left, right)
        dfs(root)
        return self.balance





    


