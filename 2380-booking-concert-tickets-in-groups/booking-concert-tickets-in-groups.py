class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m

        size = 1
        while size < n:
            size <<= 1

        self.size = size
        self.sum_tree = [0] * (2 * size)
        self.max_tree = [0] * (2 * size)

        # remaining seats in each row
        self.free = [m] * n

        for i in range(n):
            pos = size + i
            self.sum_tree[pos] = m
            self.max_tree[pos] = m

        for i in range(size - 1, 0, -1):
            self.sum_tree[i] = self.sum_tree[i * 2] + self.sum_tree[i * 2 + 1]
            self.max_tree[i] = max(
                self.max_tree[i * 2],
                self.max_tree[i * 2 + 1]
            )

        self.first = 0

    def _update(self, row: int):
        pos = self.size + row

        self.sum_tree[pos] = self.free[row]
        self.max_tree[pos] = self.free[row]

        pos //= 2

        while pos:
            self.sum_tree[pos] = (
                self.sum_tree[pos * 2]
                + self.sum_tree[pos * 2 + 1]
            )

            self.max_tree[pos] = max(
                self.max_tree[pos * 2],
                self.max_tree[pos * 2 + 1]
            )

            pos //= 2

    def _prefix_sum(self, right: int) -> int:
        left = self.size
        right += self.size

        total = 0

        while left <= right:
            if left & 1:
                total += self.sum_tree[left]
                left += 1

            if not right & 1:
                total += self.sum_tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def _find_row(self, k: int, maxRow: int) -> int:
        # No row has enough consecutive seats
        if self.max_tree[1] < k:
            return -1

        node = 1
        left = 0
        right = self.size - 1

        while node < self.size:
            mid = (left + right) // 2
            left_child = node * 2

            if left <= maxRow and self.max_tree[left_child] >= k:
                node = left_child
                right = mid
            else:
                node = left_child + 1
                left = mid + 1

        row = node - self.size

        if row >= self.n or row > maxRow:
            return -1

        return row

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self._find_row(k, maxRow)

        if row == -1:
            return []

        start_seat = self.m - self.free[row]

        self.free[row] -= k
        self._update(row)

        while self.first < self.n and self.free[self.first] == 0:
            self.first += 1

        return [row, start_seat]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._prefix_sum(maxRow) < k:
            return False

        row = self.first

        while k > 0:
            take = min(k, self.free[row])

            self.free[row] -= take
            k -= take

            self._update(row)

            if self.free[row] == 0:
                row += 1
            else:
                break

        self.first = row

        while self.first < self.n and self.free[self.first] == 0:
            self.first += 1

        return True