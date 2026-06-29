# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        dfs
        each iteration -> targetSum - curr.val


        dfs call -> if are at leaf and curr.val == targetVal -> return true
        '''

        def dfs(node, targetSum):
            if not node:
                return False
            
            if not node.left and not node.right:
                return node.val == targetSum
            
            left = dfs(node.left, targetSum - node.val)
            right = dfs(node.right, targetSum - node.val)

            return left or right
        return dfs(root, targetSum)