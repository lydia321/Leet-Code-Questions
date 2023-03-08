# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root,Max,Min):
            if not root:
                return
            self.res = max(self.res, abs(root.val - Min), abs(root.val  - Max))
            Min = min(root.val, Min)
            Max = max(root.val, Max)
            
            if root.left:
                dfs(root.left,Max,Min)
            if root.right:
                dfs(root.right,Max,Min)
        
        dfs(root,root.val,root.val)
        return self.res