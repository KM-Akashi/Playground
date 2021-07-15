class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            res = list()
            if root is not None:
                res.extend(dfs(root.left))
                res.append(root.val)
                res.extend(dfs(root.right))
            return res

        return dfs(root)