# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """

        -inf < left node < curr node < right node < inf
        """

        def dfs(leftNodeVal, node, rightNodeVal):
            if not node:
                return True
            if not leftNodeVal < node.val < rightNodeVal:
                return False

            left = dfs(leftNodeVal, node.left, node.val)
            right = dfs(node.val, node.right, rightNodeVal)

            return left and right
        return dfs(float("-inf"), root, float("inf"))