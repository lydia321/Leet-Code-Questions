# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def dfs(root):
            #Base Case
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            left,right = max(0,left),max(0,right)
            
            curr_path = left + right + root.val    
            self.res = max(self.res,curr_path)
            return root.val + max(left,right)
        
        dfs(root)
        return self.res