# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root]
        flag = True
        if not root:
            return []
        while queue:
            curr = []
            for i in range(len(queue)):
                vall = queue.pop(0)
                curr.append(vall.val)
                if vall.left:
                    queue.append(vall.left)
                if vall.right:
                    queue.append(vall.right)
            if flag:
                res.append(curr)
                flag = False
            else:
                res.append(curr[::-1])    
                flag = True
        # print(res)
        return res
   