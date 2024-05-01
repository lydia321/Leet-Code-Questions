class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete_set = set(to_delete)
        
        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            if root.val in to_delete_set:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                return None
            return root

    
        final = dfs(root)
        if final:
            res.append(final)
        return res
        