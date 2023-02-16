"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        res = []
        queue = [root]
        
        while queue:
            curr = []
            for _ in range(len(queue)):
                val = queue.pop(0)
                curr.append(val.val)
                
                if val.children:
                    for child in val.children:
                        queue.append(child)
            res.append(curr)
                
            
        
        return res