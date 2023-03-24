# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = '{}'
    
        def dfs(root,curr,n):
            if not root.left and not root.right:
                self.res =  min(self.res, chr(root.val + 97) + curr)
            if root.left:
                dfs(root.left, chr(root.val + 97) + curr, n + root.val)
            if root.right:
                dfs(root.right, chr(root.val + 97)+ curr, n + root.val)
      
        dfs(root,'',0)
        return self.res