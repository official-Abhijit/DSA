class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        count = 0

        for x in range(201):
            for y in range(201):
                for cx, cy, r in circles:
                    dx = x - cx
                    dy = y - cy

                    if dx * dx + dy * dy <= r * r:
                        count += 1
                        break

        return count