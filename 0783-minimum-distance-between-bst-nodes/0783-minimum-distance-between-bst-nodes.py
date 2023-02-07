# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root: return
        queue = [root]
        val = []
        while queue:
            
            for _ in range(len(queue)):
                curr = queue.pop(0)
                val.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    # val.append(curr.left.val)
                    # minn = min(minn,abs(curr.val - curr.left.val))
                if curr.right:
                    queue.append(curr.right)
                    # val.append(curr.right.val)
                    # minn = min(minn,abs(curr.val - curr.right.val))
        val.sort()
        print(val)
        minn, l, r = float('inf'), 0, 1
        while r < len(val):
            minn = min(minn, (val[r] - val[l]))
            l += 1
            r += 1
        return minn