# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        need to pass the maxNodeVal seen so far

        good nodes = left good nodes + right good nodes + if current node is good or not
        """

        def dfs(node, maxVal):
            if not node:
                return 0
            
            currNodeGood = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            return dfs(node.left, maxVal) + dfs(node.right, maxVal) + currNodeGood
        
        return dfs(root,root.val)