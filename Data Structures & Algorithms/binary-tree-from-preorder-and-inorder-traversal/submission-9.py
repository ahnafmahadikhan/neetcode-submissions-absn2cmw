class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {v: i for i, v in enumerate(inorder)}
        n = len(preorder)
        pre = 0

        def dfs(l, r):
            nonlocal pre

            if l > r:
                return None

            val = preorder[pre]
            pre += 1

            node = TreeNode(val)
            m = pos[val]

            node.left = dfs(l, m - 1)
            node.right = dfs(m + 1, r)

            return node

        return dfs(0, n - 1)