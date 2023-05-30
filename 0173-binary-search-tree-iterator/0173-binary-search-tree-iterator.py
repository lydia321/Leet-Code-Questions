# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = [-inf]
        queue = [root]
        while queue:
            curr = queue.pop()
            self.arr.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        self.arr.sort()
        self.ptr = 0
    def next(self) -> int:
        self.ptr += 1
        return self.arr[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr != len(self.arr) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()