class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        answer = float("inf")

        for i, card in enumerate(cards):
            if card in last_seen:
                length = i - last_seen[card] + 1
                answer = min(answer, length)

            last_seen[card] = i

        return answer if answer != float("inf") else -1