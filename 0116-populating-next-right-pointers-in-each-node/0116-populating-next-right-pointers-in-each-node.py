"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #BFS Approach
        if not root:
            return
        queue = [root]
        
        
        while queue:
            length = len(queue) -1
            for i in range(len(queue)):
                curr = queue.pop(0)
                
                if i < length:
                    curr.next = queue[0]
                else:
                    curr.next = None
                    
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root