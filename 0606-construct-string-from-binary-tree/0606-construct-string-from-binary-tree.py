# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = ''
        
        def dfs(root):
            if not root:
                return
            self.res += '(' + str(root.val)
            if root.left:
                dfs(root.left)
            if not root.left and root.right:
                self.res += '()'
            if root.right:
                dfs(root.right)
            self.res += ')'
        
        dfs(root)
        return self.res[1:-1]
       