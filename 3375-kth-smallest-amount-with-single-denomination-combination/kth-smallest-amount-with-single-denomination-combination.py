from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        useful = []

        for coin in coins:
            if not any(coin % x == 0 for x in useful):
                useful.append(coin)

        coins = useful
        m = len(coins)

        coefficient = {}

        def build(index, current_lcm, used):
            for i in range(index, m):
                g = gcd(current_lcm, coins[i])
                new_lcm = current_lcm // g * coins[i]

                sign = 1 if used % 2 == 0 else -1
                coefficient[new_lcm] = coefficient.get(new_lcm, 0) + sign

                build(i + 1, new_lcm, used + 1)

        build(0, 1, 0)

        terms = []

        for lcm, sign in coefficient.items():
            if sign != 0:
                terms.append((lcm, sign))

        def count(amount):
            total = 0

            for lcm, sign in terms:
                total += sign * (amount // lcm)

            return total

        left = 1
        right = coins[0] * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left