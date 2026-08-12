from bisect import insort

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        best_seat = 0
        best_dist = self.seats[0]

        for i in range(1, len(self.seats)):
            left = self.seats[i - 1]
            right = self.seats[i]

            seat = (left + right) // 2
            dist = seat - left

            if dist > best_dist:
                best_dist = dist
                best_seat = seat

        # Check the gap after the last occupied seat
        last_dist = self.n - 1 - self.seats[-1]

        if last_dist > best_dist:
            best_seat = self.n - 1

        insort(self.seats, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)