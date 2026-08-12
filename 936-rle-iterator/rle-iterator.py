class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.encoding):
            count = self.encoding[self.i]

            if count >= n:
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]

            n -= count
            self.i += 2

        return -1