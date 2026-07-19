# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''

                    -10
            9				20
                        15		7
    42 -> 20, 15, 7

    Cases:
    keep both left and right subtree sums + current node val (20, 15 ,7)-> See if this is the max path sum 
    keep either left or right + current node val ->  ignore negatives
    neither subtree, just the current node val  -> both subtrees might be negative

    DFS recursion
        return if empty
        
        maxSum -> max(maxSum or curr.node + left + right)
        
        see which subtree gives larger path sum with current node value
        
    Time Complexity: O(N) - Every node needs to be visited to calculate the max sum, so O(N) time is used. 
    Space Complexity: O(N) - Space used is based on recursion stack of DFS. Best case is the tree is balanced so the space used would be the height of tree, O(H). Worst case is the tree is linearly linked, so O(N).
    Time spent on problem: 30 minutes
    '''
    def maxPathSum(self, root: Optional["TreeNode"]) -> int:
        self.maxSum = float("-inf") # possibility that a negative could be the max sum

        def dfs(node):
            if node is None:
                return 0
            left = max(dfs(node.left), 0) # ignore negatives
            right = max(dfs(node.right), 0)

            #check if curr node + left + right is max
            self.maxSum = max(self.maxSum, left + right + node.val)

            return max(left, right) + node.val
        dfs(root)
        return self.maxSum
            