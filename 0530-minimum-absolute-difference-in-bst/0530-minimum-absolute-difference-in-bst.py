# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.diff = float('inf')
        self.Min = float('-inf')
        
        def dfs(root):
            if root:
                dfs(root.left)
                self.diff = min(self.diff, abs(self.Min - root.val))
                self.Min = root.val
                dfs(root.right)
        
        dfs(root)
        return self.diff