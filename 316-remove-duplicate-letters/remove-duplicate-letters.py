class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}

        for i, char in enumerate(s):
            last[char] = i

        stack = []
        used = set()

        for i, char in enumerate(s):
            if char in used:
                continue

            while (
                stack
                and char < stack[-1]
                and last[stack[-1]] > i
            ):
                removed = stack.pop()
                used.remove(removed)

            stack.append(char)
            used.add(char)

        return "".join(stack)