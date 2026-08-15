from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        self.data = {}  # key -> [value, freq]
        self.freq = defaultdict(OrderedDict)

    def _touch(self, key):
        value, f = self.data[key]

        del self.freq[f][key]

        if not self.freq[f]:
            del self.freq[f]

            if self.min_freq == f:
                self.min_freq += 1

        f += 1
        self.freq[f][key] = None
        self.data[key][1] = f

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        value = self.data[key][0]
        self._touch(key)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.data:
            self.data[key][0] = value
            self._touch(key)
            return

        if len(self.data) == self.capacity:
            old_key, _ = self.freq[self.min_freq].popitem(last=False)

            if not self.freq[self.min_freq]:
                del self.freq[self.min_freq]

            del self.data[old_key]

        self.data[key] = [value, 1]
        self.freq[1][key] = None
        self.min_freq = 1