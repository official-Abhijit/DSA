class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)

        while area % width != 0:
            width -= 1

        length = area // width

        return [length, width]