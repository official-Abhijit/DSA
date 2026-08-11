class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.values = []

        self.multiply = 1
        self.add = 0

    def append(self, val: int) -> None:
        inverse = pow(self.multiply, self.MOD - 2, self.MOD)

        original = (val - self.add) * inverse % self.MOD
        self.values.append(original)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.multiply = self.multiply * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1

        return (
            self.values[idx] * self.multiply + self.add
        ) % self.MOD