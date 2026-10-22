# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        track if subtree on left and right of node are balanced
        track the height of each subtree

        return two values [bool balanced, max height of subtree]

        balanced is true if left and right are true + their diff is <= 1

        need to return the max height of either left or right subtree
        """

        def dfs(node):
            if not node:
                return [True, 0] # base case. empty tree is balanced
            
            left = dfs(node.left)
            right = dfs(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced,1 +max(left[1], right[1])]

        return dfs(root)[0]