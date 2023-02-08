# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return
        queue = [[root,root.val]]

        while queue:
            for _ in range(len(queue)):
                curr,Sum = queue.pop(0)
                if Sum == targetSum and not curr.left and not curr.right:
                    return True
                if curr.left:
                    queue.append([curr.left, Sum + curr.left.val])
                if curr.right:
                    queue.append([curr.right, Sum + curr.right.val])
                   
        return False
        