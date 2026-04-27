# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        longest path of any given nodes is the left + right subtree

        dfs

        basecase -> if not node: return 0

        left = dfs(node.left)
        right = dfs(node.right)

        len_sum = left + right
        self.maxRes = max(maxRes, len_sum)

        return max(left, right)


        """

        self.maxRes = 0

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            len_sum = left + right
            self.maxRes = max(self.maxRes, len_sum)

            return 1 + max(left, right)
        
        dfs(root)
        return self.maxRes


