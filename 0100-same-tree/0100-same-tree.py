# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = [p]
        queue2 = [q]
        if p and not q: return False
        if q and not p: return False
        if not q and not p: return True
        while queue1 and queue2:
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)
            if curr1.val != curr2.val:
                return False
            if curr1.left and curr2.left:
                queue1.append(curr1.left)
                queue2.append(curr2.left)
            elif curr1.left or curr2.left:
                return False
            
            if curr1.right and curr2.right:
                queue1.append(curr1.right)
                queue2.append(curr2.right)
            elif curr1.right or curr2.right:
                return False
        return True