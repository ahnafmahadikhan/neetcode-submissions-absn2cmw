class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {value: i for i, value in enumerate(inorder)}
        preIndex = 0

        def dfs(left, right):
            nonlocal preIndex

            if left > right:
                return None

            root_val = preorder[preIndex]
            preIndex += 1

            root = TreeNode(root_val)
            mid = pos[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)