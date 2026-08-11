class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        missing = 0
        if not any(c.islower() for c in password):
            missing += 1
        if not any(c.isupper() for c in password):
            missing += 1
        if not any(c.isdigit() for c in password):
            missing += 1

        groups = []
        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                groups.append(length)

            i = j

        # Too short
        if n < 6:
            return max(missing, 6 - n)

        replacements = sum(length // 3 for length in groups)

        # Length is already valid
        if n <= 20:
            return max(missing, replacements)

        # Too long: deletions are required
        delete = n - 20
        remaining_delete = delete

        # Best groups to delete from first:
        # len % 3 == 0 -> 1 deletion saves 1 replacement
        for idx in range(len(groups)):
            if remaining_delete == 0:
                break

            if groups[idx] % 3 == 0:
                groups[idx] -= 1
                remaining_delete -= 1

        # len % 3 == 1 -> 2 deletions save 1 replacement
        for idx in range(len(groups)):
            if remaining_delete < 2:
                break

            if groups[idx] % 3 == 1:
                take = min(2, remaining_delete)
                groups[idx] -= take
                remaining_delete -= take

        # Any 3 deletions save 1 replacement
        for idx in range(len(groups)):
            if remaining_delete == 0:
                break

            if groups[idx] >= 3:
                take = min(
                    groups[idx] - 2,
                    remaining_delete
                )

                groups[idx] -= take
                remaining_delete -= take

        replacements = sum(length // 3 for length in groups)

        return delete + max(missing, replacements)