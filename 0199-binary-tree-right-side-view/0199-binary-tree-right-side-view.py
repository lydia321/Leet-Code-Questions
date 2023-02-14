# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        queue = [root]
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right :
                    queue.append(curr.right)
            # print(queue,res)
            if queue: res.append(queue[-1].val)
        return res            
        
        