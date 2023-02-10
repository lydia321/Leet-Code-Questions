# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return
        queue = [root]
        
        while queue: 
            for _ in range(len(queue)):
                curr = queue.pop(0)
                # print(curr.val)
                if curr.left:
                    print(0)
                    queue.append(curr.left)
                    if not curr.left.right and not curr.left.left:
                        res += curr.left.val
                if curr.right:
                    queue.append(curr.right)
            
        
        return res