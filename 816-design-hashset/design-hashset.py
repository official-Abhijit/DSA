class MyHashSet:

    def __init__(self):
        self.present = bytearray(1_000_001)

    def add(self, key: int) -> None:
        self.present[key] = 1

    def remove(self, key: int) -> None:
        self.present[key] = 0

    def contains(self, key: int) -> bool:
        return self.present[key] == 1