# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root,Min,Max):
            if not root:
                return 
            self.res = max(self.res, abs(root.val - Min), abs(root.val - Max))
            Max = max(Max, root.val)
            Min = min(Min, root.val)
            if root.left:
                dfs(root.left,Min,Max)
            if root.right:
                dfs(root.right,Min,Max)
        dfs(root,root.val,root.val)
        return self.res