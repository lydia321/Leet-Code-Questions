# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.m = root.val
        self.res = float('inf')
        
        def dfs(root):
            if not root:
                return
            if self.m < root.val < self.res:
                self.res = root.val
                        
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.res if self.res != float('inf') else -1