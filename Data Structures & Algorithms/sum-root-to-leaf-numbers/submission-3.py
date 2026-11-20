# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        need to pass the currnet digits seen so far

        pass upwards the value of the sum
        """

        def dfs(node, pathNums):
            if not node:
                return 0
            
            pathNums = pathNums * 10 + node.val

            if not node.left and not node.right:
                return pathNums
            left = dfs(node.left, pathNums)
            right = dfs(node.right, pathNums)

            return left + right
        return dfs(root, 0)