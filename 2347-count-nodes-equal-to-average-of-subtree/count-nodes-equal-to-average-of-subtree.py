class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                answer += 1

            return total_sum, total_count

        dfs(root)
        return answer