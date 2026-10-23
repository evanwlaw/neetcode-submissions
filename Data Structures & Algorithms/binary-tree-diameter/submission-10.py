# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        return longest path between any 2 nodes in tree.
        so need to keep max total -> see if left + right paths through node is largest

        pass upwards, max(leftsubtree, right subtree) + 1
        """
        output = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal output
            
            left, right = dfs(node.left), dfs(node.right)
            #check if we found longest path via current node
            output = max(output, left + right)

            return 1 + max(left,right)
        
        dfs(root)
        return output
