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
        if not root:
                return None
        curr = root
        Next_curr = curr.left
        
        while curr and Next_curr:
            
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = Next_curr
                Next_curr = curr.left
        return root
        
            
        
        
        #O(N) time complexity and O(N) Space complexity
#         if not root:
#             return
#         queue = [root]
        
#         while queue:
#             length = len(queue)
            
#             for i in range(length):
#                 curr = queue.pop(0)
                
#                 if i < length - 1:
#                     curr.next = queue[0]
#                 else:
#                     curr.next = None
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#         return root