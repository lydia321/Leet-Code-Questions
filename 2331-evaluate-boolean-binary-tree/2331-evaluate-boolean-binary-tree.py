# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.left:
                return root.val
            
            a = dfs(root.left)
            b = dfs(root.right)
            
            if root.val == 3:
                return a and b
            
            return a or b
            
        return dfs(root)
        