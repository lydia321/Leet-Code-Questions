"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        
        def dfs(root):
            #BaseCase
            if not root:
                return
            for child in root.children:
                dfs(child)
                self.res.append(child.val)
            
        dfs(root)
        if root: self.res.append(root.val)
        return self.res
     