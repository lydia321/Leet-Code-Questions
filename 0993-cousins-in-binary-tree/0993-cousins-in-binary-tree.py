# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        self.a = None
        self.b = None
        
        def dfs(root,depth,parent):
            if not root:
                return
            if root.val == x :
                self.a = (depth,parent)
            if root.val == y :
                self.b = (depth,parent)
            dfs(root.left,depth + 1,root)
            dfs(root.right,depth +1,root)
        
        dfs(root,0,None)
        if self.a[1] != self.b[1] and self.a[0] == self.b[0]:
            return True
        return False