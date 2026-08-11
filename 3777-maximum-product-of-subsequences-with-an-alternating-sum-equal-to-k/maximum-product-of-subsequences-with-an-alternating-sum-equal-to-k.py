class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        overflow = limit + 1

        # (alternating_sum, parity) -> set of products
        # parity = 1 means next picked number will be subtracted
        # parity = 0 means next picked number will be added
        dp = {}

        for num in nums:
            new_dp = {
                state: products.copy()
                for state, products in dp.items()
            }

            # Start a new subsequence with this number
            product = num if num <= limit else overflow
            new_dp.setdefault((num, 1), set()).add(product)

            # Extend existing subsequences
            for (current_sum, parity), products in dp.items():

                if parity == 1:
                    new_sum = current_sum - num
                else:
                    new_sum = current_sum + num

                next_parity = 1 - parity

                if (new_sum, next_parity) not in new_dp:
                    new_dp[(new_sum, next_parity)] = set()

                for product in products:
                    if num == 0:
                        new_product = 0

                    elif product == overflow:
                        new_product = overflow

                    else:
                        new_product = product * num

                        if new_product > limit:
                            new_product = overflow

                    new_dp[(new_sum, next_parity)].add(new_product)

            dp = new_dp

        answer = -1

        for (current_sum, parity), products in dp.items():
            if current_sum != k:
                continue

            for product in products:
                if product <= limit:
                    answer = max(answer, product)

        return answer