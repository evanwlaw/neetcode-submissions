# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        travese level order via bfs.

        use a flag e.g. left_right to see if we need to add to res from left or from right

        '''

        queue = deque([root] if root else [])
        left_right = True
        res = []

        while queue:
            level_node = deque()

            for i in range(len(queue)):
                node = queue.popleft()
                if left_right:
                    level_node.append(node.val)
                else:
                    level_node.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(level_node)
            left_right = not left_right
        return res
