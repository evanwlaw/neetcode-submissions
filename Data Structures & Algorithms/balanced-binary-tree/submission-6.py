# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        return true/false if tree is height balanced
        True if all nodes are -> abs(leftheight - rightheight) <= 1

        to push upwards [bool balanced, height]
        """

        def dfs(node):
            if not node:
                return (True, 0)
            
            left, right = dfs(node.left), dfs(node.right)

            # if balanced
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                return (True, 1 + max(left[1], right[1]))
            
            # not balanced
            return (False, 1 + max(left[1], right[1]))
        return dfs(root)[0]

