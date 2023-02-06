# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return
        if not root1: return root2
        if not root2: return root1
        queue1 = [root1]
        queue2 = [root2]
        
        while queue1 and queue2:
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)
            curr1.val += curr2.val
                
            if curr2.left:
                if curr1.left:
                    queue1.append(curr1.left)
                    queue2.append(curr2.left)
                else:
                    curr1.left = curr2.left
                    
            if curr2.right:
                if curr1.right:
                    queue1.append(curr1.right)
                    queue2.append(curr2.right)
                else:
                    curr1.right = curr2.right
        return root1