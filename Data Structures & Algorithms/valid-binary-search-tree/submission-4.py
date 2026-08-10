# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left_value, node, right_value):
            if node is None:
                return True # empty tree is valid and balanced

            if not (left_value < node.val < right_value):
                return False

            left = dfs(left_value, node.left, node.val)
            right = dfs(node.val, node.right, right_value)
            return left and right

        return dfs(float("-inf"), root, float("inf"))