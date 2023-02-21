# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        
        def dfs(root,Min,Max):
            if not root:
                return True
            if not (Min < root.val < Max):
                self.flag = False
            #every time it goes left,its root is the upper bound
            dfs(root.left,Min,root.val)
            #every time it goes right,its root is the lower bound
            dfs(root.right,root.val,Max)
            
        dfs( root,float('-inf'),float('inf'))
        return self.flag