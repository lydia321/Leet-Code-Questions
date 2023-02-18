# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(node,parent,grand):
            if not node:
                return 0
            if grand and grand.val %2 == 0:
                self.total += node.val
            return self.total + dfs(node.left, node,parent) + dfs(node.right, node, parent)
            
        dfs(root,None,None)    
        return self.total
        
        