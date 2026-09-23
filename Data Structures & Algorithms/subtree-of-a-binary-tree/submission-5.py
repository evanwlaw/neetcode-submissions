# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        subtree in root tree needs to be the same as subroot version.

        
        """
        def checkSubtree(p, q):
            if not p and not q:
                return True

            if not p or not q or (p.val != q.val):
                return False
            
            return checkSubtree(p.left, q.left) and checkSubtree(p.right, q.right)

        def dfsScan(node):
            if not node:
                return False
            
            if checkSubtree(node, subRoot):
                return True
            return dfsScan(node.left) or dfsScan(node.right)
        
        return dfsScan(root)