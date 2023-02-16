# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        res = []
        queue = [root]
        
        while queue:
            curr = []
            
            for _ in range(len(queue)):
                val = queue.pop(0)
                curr.append(val.val)
                
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            res.append(curr)
        return res