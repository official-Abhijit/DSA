from collections import Counter

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        left = Counter()
        right = Counter()
        both = 0

        for card in cards:
            a, b = card

            if a == x and b == x:
                both += 1
            elif a == x:
                left[b] += 1
            elif b == x:
                right[a] += 1

        def best(group, extra):
            total = sum(group.values()) + extra

            if total == 0:
                return 0

            biggest = extra

            for count in group.values():
                biggest = max(biggest, count)

            return min(total // 2, total - biggest)

        answer = 0

        for use_left in range(both + 1):
            use_right = both - use_left

            points = (
                best(left, use_left) +
                best(right, use_right)
            )

            answer = max(answer, points)

        return answer