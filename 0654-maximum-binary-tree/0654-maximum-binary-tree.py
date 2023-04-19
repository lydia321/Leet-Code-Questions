# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(l,r):
            if  l > r or l < 0:
                return 
            curr_max = max(nums[l:+r+1])
            idx = nums.index(curr_max)
            if idx < 0:
                return
            res = TreeNode(curr_max)
            res.left = dfs(l,idx - 1)
            res.right = dfs(idx+1,r)
            return res
        
        return dfs(0,len(nums) - 1)
