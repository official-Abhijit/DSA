class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        half = (n + 1) // 2

        # powers[i] = 10^i % k
        powers = bytearray(n)
        powers[0] = 1 % k

        for i in range(1, n):
            powers[i] = powers[i - 1] * 10 % k

        # contribution of one digit at each position in first half
        weight = bytearray(half)

        for i in range(half):
            j = n - 1 - i

            if i == j:
                weight[i] = powers[i]
            else:
                weight[i] = (powers[i] + powers[j]) % k

        # possible[pos * k + rem] tells whether positions
        # pos...half-1 can create remainder rem
        possible = bytearray((half + 1) * k)
        possible[half * k] = 1

        for pos in range(half - 1, -1, -1):
            cur = pos * k
            nxt = (pos + 1) * k
            w = weight[pos]

            for digit in range(10):
                add = digit * w % k

                for rem in range(k):
                    if possible[nxt + rem]:
                        possible[cur + (add + rem) % k] = 1

        # Greedily build the largest first half
        first_half = bytearray(half)
        remainder = 0

        for pos in range(half):
            w = weight[pos]
            start = 9
            end = 1 if pos == 0 else 0

            for digit in range(start, end - 1, -1):
                new_rem = (remainder + digit * w) % k
                need = (-new_rem) % k

                if possible[(pos + 1) * k + need]:
                    first_half[pos] = 48 + digit
                    remainder = new_rem
                    break

        # Mirror first half
        answer = bytearray(n)

        for i in range(half):
            answer[i] = first_half[i]
            answer[n - 1 - i] = first_half[i]

        return answer.decode()