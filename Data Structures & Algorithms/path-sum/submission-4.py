# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        dfs to find targetSum.
        each dfs, targetSum - node.val
        if we reach leaf node, and targetSum == 0, then we found path
        '''
        if root is None:
            return False
            
        targetSum -= root.val

        if root.left is None and root.right is None:
            return targetSum == 0

        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)

        return left or right