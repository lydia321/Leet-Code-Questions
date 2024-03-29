# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        queue = deque([root])
        i = 1
        
        while queue:
            
            for j in range(len(queue)):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if i % 2 != 0:
                l, r = 0, len(queue) - 1
                while l < r:
                    queue[l].val,queue[r].val = queue[r].val,queue[l].val
                    l += 1
                    r -= 1
            i += 1
        return root