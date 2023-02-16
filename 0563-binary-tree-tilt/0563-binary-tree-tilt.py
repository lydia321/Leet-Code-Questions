# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        
    
        def dfs(root):
            nonlocal res
            #Base Case
            if not root: return 0

            right = dfs(root.right)
            left = dfs(root.left)
            res += abs(right - left)

            return left + right + root.val
        
        dfs(root)
        return res