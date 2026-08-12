class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        mn = 10**9
        mx = 0
        fixed_gap = 0

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]

            if a != -1 and b != -1:
                fixed_gap = max(fixed_gap, abs(a - b))

            elif (a == -1) != (b == -1):
                value = b if a == -1 else a
                mn = min(mn, value)
                mx = max(mx, value)

        # No -1 touches any positive number -> all values are missing
        if mx == 0:
            return fixed_gap

        def can(d):
            x = mn + d
            y = mx - d

            i = 0

            while i < n:
                if nums[i] != -1:
                    i += 1
                    continue

                start = i

                while i < n and nums[i] == -1:
                    i += 1

                length = i - start

                left = nums[start - 1] if start > 0 else -1
                right = nums[i] if i < n else -1

                # Missing block at an edge
                if left == -1 or right == -1:
                    value = right if left == -1 else left

                    if min(abs(value - x), abs(value - y)) > d:
                        return False

                # Exactly one missing number:
                # [left, ?, right]
                elif length == 1:
                    use_x = max(abs(left - x), abs(right - x))
                    use_y = max(abs(left - y), abs(right - y))

                    if min(use_x, use_y) > d:
                        return False

                else:
                    # Fill whole block with x
                    all_x = max(abs(left - x), abs(right - x))

                    # Fill whole block with y
                    all_y = max(abs(left - y), abs(right - y))

                    # Start with x, finish with y
                    x_to_y = max(
                        abs(left - x),
                        abs(x - y),
                        abs(right - y)
                    )

                    # Start with y, finish with x
                    y_to_x = max(
                        abs(left - y),
                        abs(x - y),
                        abs(right - x)
                    )

                    if min(all_x, all_y, x_to_y, y_to_x) > d:
                        return False

            return True

        low = fixed_gap
        high = max(fixed_gap, (mx - mn + 1) // 2)

        while low < high:
            mid = (low + high) // 2

            if can(mid):
                high = mid
            else:
                low = mid + 1

        return low