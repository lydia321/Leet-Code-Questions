# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        
        while queue:
            curr_deepest = set()
            for _ in range(len(queue)):
                curr = queue.pop(0)
                curr_deepest.add(curr)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        if len(curr_deepest) == 1:
            return curr_deepest.pop()
       
        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            
            if (left and right) or (root in curr_deepest):
                return root
            else:
                return left or right
            
        return dfs(root)