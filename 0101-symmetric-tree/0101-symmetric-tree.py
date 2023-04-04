# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root: return True
        queue = [root]
        left_queue = []
        right_queue = []
        A = queue.pop()
        if not A.left and not A.right:
            return True
        if A.left: 
            left_queue.append(A.left)
        else: return False
        if A.right:
            right_queue.append(A.right)
        else: return False
       
        
        while left_queue and right_queue:
            curr1 = left_queue.pop()
            curr2 = right_queue.pop()
            # print(curr1,curr2)
            if not curr1 and not curr2: continue
            if not curr1 or not curr2: return False
            
            if curr1.val != curr2.val:
                return False
            left_queue.append(curr1.right)
            left_queue.append(curr1.left)
            right_queue.append(curr2.left)
            right_queue.append(curr2.right)
        if len(left_queue) == len(right_queue):
            return True
        return False
   