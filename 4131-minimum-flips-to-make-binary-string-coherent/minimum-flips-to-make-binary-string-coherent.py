class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones

        # Make everything 0
        answer = ones

        # Keep exactly one 1
        if ones > 0:
            answer = min(answer, ones - 1)

        # Make everything 1
        answer = min(answer, zeros)

        # Exactly two 1s:
        # target must be 100...001
        if n >= 2:
            cost = 0

            if s[0] == '0':
                cost += 1
            if s[-1] == '0':
                cost += 1

            for i in range(1, n - 1):
                if s[i] == '1':
                    cost += 1

            answer = min(answer, cost)

        return answer