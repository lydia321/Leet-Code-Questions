# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(grand, parent, node):
            # print("Grand", grand.val if grand else None,"Parent", parent.val if parent else None,"Node", node.val if node else None)
            if not node:
                return 0

            total = 0
            if grand and grand.val % 2 == 0:
                total += node.val

            return total + dfs(parent, node, node.left) + dfs(parent, node, node.right)
        
        return dfs(None, None, root)