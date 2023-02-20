# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = [root]
        flag = False
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.val == val:
                    flag = True
                    return curr
                else:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
       
                            