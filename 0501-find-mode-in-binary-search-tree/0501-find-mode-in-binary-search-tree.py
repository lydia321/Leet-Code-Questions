# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        res = []
        visited = defaultdict(int)
        queue = [root]
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop()
                if curr.val in visited:
                    if curr.val not in res: res.append(curr.val)
                visited[curr.val] += 1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        val = 0
        for i,count in visited.items():
            if count > val:
                val = count
                res = [i]
            elif count == val:
                res.append(i)
        return res
    
    
        