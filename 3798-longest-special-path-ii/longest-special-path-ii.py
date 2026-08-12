import sys
sys.setrecursionlimit(100000)

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        last = [-1] * 50001
        path_dist = []

        best_length = 0
        min_nodes = 1

        def dfs(node, parent, dist, largest, second):
            nonlocal best_length, min_nodes

            depth = len(path_dist)
            path_dist.append(dist)

            value = nums[node]
            prev = last[value]

            # A repeated value creates a duplicate event
            # at its previous occurrence position.
            if prev != -1:
                if prev > largest:
                    second = largest
                    largest = prev
                elif prev > second:
                    second = prev

            # Remove everything through the second-largest
            # duplicate event. One duplicate is allowed to remain.
            left = second + 1

            length = dist - path_dist[left]
            nodes = depth - left + 1

            if length > best_length:
                best_length = length
                min_nodes = nodes
            elif length == best_length:
                min_nodes = min(min_nodes, nodes)

            old = last[value]
            last[value] = depth

            for nxt, weight in graph[node]:
                if nxt != parent:
                    dfs(
                        nxt,
                        node,
                        dist + weight,
                        largest,
                        second
                    )

            last[value] = old
            path_dist.pop()

        dfs(0, -1, 0, -1, -1)

        return [best_length, min_nodes]