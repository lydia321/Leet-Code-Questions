# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        if not root: return []
        
        while queue:
            level_sum = 0
            curr_len = len(queue)
            
            for i in range(len(queue)):
                curr = queue.pop(0)
                level_sum += curr.val
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level_avg = level_sum/curr_len
            res.append(level_avg)
        return res
    