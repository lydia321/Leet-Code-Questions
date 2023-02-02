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
        queue1 = []
        queue2 = []
        A = queue.pop()
        if not A.left and not A.right:
            return True
        if A.left: 
            queue1.append(A.left)
        else: return False
        if A.right:
            queue2.append(A.right)
        else: return False
        if A.left.val != A.right.val: return False    
        
        while queue1 and queue2:
            curr1 = queue1.pop()
            curr2 = queue2.pop()
            # print(curr1,curr2)
            if not curr1 and not curr2: continue
            if not curr1 or not curr2: return False
            
            if curr1.val != curr2.val:
                return False
            queue1.append(curr1.right)
            queue1.append(curr1.left)
            queue2.append(curr2.left)
            queue2.append(curr2.right)
        if len(queue1) == len(queue2):
            return True
        return False
   