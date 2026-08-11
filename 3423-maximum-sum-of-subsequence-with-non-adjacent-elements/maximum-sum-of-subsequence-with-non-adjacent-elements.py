class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [[0, 0, 0, 0] for _ in range(4 * n)]

        def build(node, left, right):
            if left == right:
                val = max(0, nums[left])

                # 00, 01, 10, 11
                tree[node] = [0, 0, 0, val]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def merge(a, b):
            res = [0] * 4

            # left not selected, right not selected
            res[0] = max(
                a[0] + b[0],
                a[0] + b[2],
                a[1] + b[0]
            )

            # left not selected, right selected
            res[1] = max(
                a[0] + b[1],
                a[0] + b[3],
                a[1] + b[1]
            )

            # left selected, right not selected
            res[2] = max(
                a[2] + b[0],
                a[2] + b[2],
                a[3] + b[0]
            )

            # left selected, right selected
            res[3] = max(
                a[2] + b[1],
                a[2] + b[3],
                a[3] + b[1]
            )

            return res

        def update(node, left, right, pos, value):
            if left == right:
                val = max(0, value)
                tree[node] = [0, 0, 0, val]
                return

            mid = (left + right) // 2

            if pos <= mid:
                update(node * 2, left, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, right, pos, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        answer = 0

        for pos, value in queries:
            update(1, 0, n - 1, pos, value)

            best = max(tree[1])
            answer = (answer + best) % MOD

        return answer