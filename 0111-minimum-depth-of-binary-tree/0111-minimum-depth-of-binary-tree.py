# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        levels = {root: 0}
        
        while queue:
            curr = queue.pop(0)
            if not curr: return 0
            if not curr.left and not curr.right:
                return levels[curr] + 1
            if curr.left:
                queue.append(curr.left)
                levels[curr.left] = levels[curr] + 1
            if curr.right:
                queue.append(curr.right)
                levels[curr.right] = levels[curr] + 1
                
            