class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(current):
            if current in clones:
                return clones[current]

            copy = Node(current.val)
            clones[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)