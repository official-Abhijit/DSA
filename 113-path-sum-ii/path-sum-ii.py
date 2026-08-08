class Solution:
    def pathSum(
        self,
        root: Optional[TreeNode],
        targetSum: int
    ) -> List[List[int]]:

        result = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                if remaining == node.val:
                    result.append(path.copy())
            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            path.pop()

        dfs(root, targetSum)
        return result