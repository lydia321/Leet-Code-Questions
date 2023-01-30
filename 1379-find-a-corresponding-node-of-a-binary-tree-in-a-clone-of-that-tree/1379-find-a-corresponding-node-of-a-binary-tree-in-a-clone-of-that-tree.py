# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [original]
        clone = [cloned]
        while queue:
            
            for _ in range(len(queue)):
                curr = queue.pop(0)
                curr_clone = clone.pop(0)
                if curr is target:
                    return curr_clone
                if curr.left:
                    queue.append(curr.left)
                    clone.append(curr_clone.left)
                if curr.right:
                    queue.append(curr.right)
                    clone.append(curr_clone.right)
            
        