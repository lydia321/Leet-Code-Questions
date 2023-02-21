# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
       
        def dfs(root,curr_max):
            if root.val >= curr_max:
                self.count += 1
                curr_max = root.val
            if root.left:
                dfs(root.left,curr_max)
            if root.right:
                dfs(root.right,curr_max)                     
        dfs(root,root.val)
        return self.count