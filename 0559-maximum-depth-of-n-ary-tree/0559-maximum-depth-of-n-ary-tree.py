"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        res = 0
        queue =[root]
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for i in curr.children:
                    queue.append(i)
            res += 1
        return res
        
        