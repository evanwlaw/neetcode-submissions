# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """

    basecase: 
    if not p and not q -> true
    
    if not p or not q -> false
    if p.val != q.val -> false

    then check recurse:
        return check if left subtree AND right subtree
    

    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))