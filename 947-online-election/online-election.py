from bisect import bisect_right

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []

        count = {}
        leader = -1
        best = 0

        for person in persons:
            count[person] = count.get(person, 0) + 1

            # >= handles the tie rule:
            # the most recent vote wins
            if count[person] >= best:
                best = count[person]
                leader = person

            self.leaders.append(leader)

    def q(self, t: int) -> int:
        index = bisect_right(self.times, t) - 1
        return self.leaders[index]