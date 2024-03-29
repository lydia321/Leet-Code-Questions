# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root,curr_num):
            if root.left:
                dfs(root.left, curr_num + str(root.val))
            if root.right:
                dfs(root.right, curr_num + str(root.val))
            
            if not root.left and not root.right:
                self.res += int(curr_num + str(root.val))
            
        dfs(root,'')
        return self.res