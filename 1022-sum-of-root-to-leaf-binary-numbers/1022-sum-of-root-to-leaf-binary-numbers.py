# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root,curr_string):
            if not root.left and not root.right:
                self.res += int(curr_string + str(root.val),2)
                return 
            if root.left:
                dfs(root.left, curr_string + str(root.val))
            if root.right:
                dfs(root.right,curr_string + str(root.val))
        
        dfs(root,' ')
        return self.res