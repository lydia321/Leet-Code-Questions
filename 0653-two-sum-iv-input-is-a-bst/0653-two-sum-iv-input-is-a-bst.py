# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dict = set()
        queue = [root]
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                diff = k - curr.val
                # print(dict,diff)
                if curr.val in dict:
                    return True
                else: 
                    dict.add(diff)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return False