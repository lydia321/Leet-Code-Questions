# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0,0
            left,count1 = dfs(root.left)
            right,count2 = dfs(root.right)
            total_count = count1 + count2 + 1
            total_sum = left + right + root.val
            curr = (total_sum)//(total_count)
            if curr == root.val:
                self.res += 1
            return total_sum, total_count
        dfs(root)
        return self.res