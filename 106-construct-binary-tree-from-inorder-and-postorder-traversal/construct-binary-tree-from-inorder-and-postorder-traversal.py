class Solution:
    def buildTree(
        self,
        inorder: List[int],
        postorder: List[int]
    ) -> Optional[TreeNode]:

        inorder_index = {value: i for i, value in enumerate(inorder)}
        post_index = len(postorder) - 1

        def build(left, right):
            nonlocal post_index

            if left > right:
                return None

            root_val = postorder[post_index]
            post_index -= 1

            root = TreeNode(root_val)

            mid = inorder_index[root_val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)