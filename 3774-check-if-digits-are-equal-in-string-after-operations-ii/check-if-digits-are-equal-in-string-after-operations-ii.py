class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s) - 2

        comb5 = [
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 2, 1, 0, 0],
            [1, 3, 3, 1, 0],
            [1, 4, 6, 4, 1]
        ]

        def mod5(a, b):
            result = 1

            while a or b:
                x = a % 5
                y = b % 5

                if y > x:
                    return 0

                result = result * comb5[x][y] % 5

                a //= 5
                b //= 5

            return result

        def mod10(a, b):
            # C(a, b) mod 2
            r2 = 1 if (b & ~a) == 0 else 0

            # C(a, b) mod 5
            r5 = mod5(a, b)

            # Number must be r5 mod 5 and r2 mod 2
            if r5 % 2 == r2:
                return r5

            return r5 + 5

        diff = 0

        for i in range(n + 1):
            coefficient = mod10(n, i)

            diff += coefficient * (int(s[i]) - int(s[i + 1]))
            diff %= 10

        return diff == 0