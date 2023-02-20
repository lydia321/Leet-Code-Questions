# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
       
        def dfs(root,depth):
            if root.val >= depth:
                self.count += 1
                depth = root.val
            if root.left:
                dfs(root.left,depth)
            if root.right:
                dfs(root.right,depth)                     
        dfs(root,root.val)
        return self.count