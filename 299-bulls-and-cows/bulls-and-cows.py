class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = [0] * 10
        bulls = cows = 0

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                continue

            a = ord(s) - 48
            b = ord(g) - 48

            if count[a] < 0:
                cows += 1
            if count[b] > 0:
                cows += 1

            count[a] += 1
            count[b] -= 1

        return f"{bulls}A{cows}B"