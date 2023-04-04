# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                arr.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        arr.sort()
        # print(arr)
        
        def dfs(l,r):
            if l > r:
                return
            m = (l + r)//2
            res = TreeNode(arr[m])
            res.left = dfs(l,m-1)
            res.right = dfs(m+1,r)
            return res
        return dfs(0,len(arr) - 1)
      
        