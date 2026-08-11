class Solution:
    def longestBalanced(self, s: str) -> int:
        total_zero = s.count("0")
        total_one = len(s) - total_zero

        positions = {0: [-1]}
        prefix = 0
        answer = 0

        for i, ch in enumerate(s):
            if ch == "1":
                prefix += 1
            else:
                prefix -= 1

            if prefix not in positions:
                positions[prefix] = []

            positions[prefix].append(i)

            # Already balanced
            answer = max(answer, i - positions[prefix][0])

            # Two more 1s than 0s
            if prefix - 2 in positions:
                prev = positions[prefix - 2]

                zeros_inside = (i - prev[0] - 2) // 2

                if zeros_inside < total_zero:
                    answer = max(answer, i - prev[0])
                elif len(prev) > 1:
                    answer = max(answer, i - prev[1])

            # Two more 0s than 1s
            if prefix + 2 in positions:
                prev = positions[prefix + 2]

                ones_inside = (i - prev[0] - 2) // 2

                if ones_inside < total_one:
                    answer = max(answer, i - prev[0])
                elif len(prev) > 1:
                    answer = max(answer, i - prev[1])

        return answer