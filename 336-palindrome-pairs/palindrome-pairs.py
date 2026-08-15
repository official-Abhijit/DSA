class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def palindrome_info(s):
            n = len(s)

            prefix = [False] * (n + 1)
            suffix = [False] * (n + 1)

            prefix[0] = True
            suffix[n] = True

            # odd length palindromes
            d1 = [0] * n
            l, r = 0, -1

            for i in range(n):
                k = 1 if i > r else min(d1[l + r - i], r - i + 1)

                while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                    k += 1

                d1[i] = k

                left = i - k + 1
                right = i + k - 1

                if left == 0:
                    prefix[right + 1] = True

                if right == n - 1:
                    suffix[left] = True

                if i + k - 1 > r:
                    l = i - k + 1
                    r = i + k - 1

            # even length palindromes
            d2 = [0] * n
            l, r = 0, -1

            for i in range(n):
                k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)

                while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                    k += 1

                d2[i] = k

                if k:
                    left = i - k
                    right = i + k - 1

                    if left == 0:
                        prefix[right + 1] = True

                    if right == n - 1:
                        suffix[left] = True

                if i + k - 1 > r:
                    l = i - k
                    r = i + k - 1

            return prefix, suffix

        # Compact trie representation
        next_node = {}
        terminal = [-1]
        pal_words = {}

        prefix_info = []
        suffix_info = []

        for word in words:
            pref, suff = palindrome_info(word)
            prefix_info.append(pref)
            suffix_info.append(suff)

        # Insert every word backwards
        for idx, word in enumerate(words):
            node = 0
            pref = prefix_info[idx]

            for i in range(len(word) - 1, -1, -1):
                if pref[i + 1]:
                    pal_words.setdefault(node, []).append(idx)

                key = (node, word[i])

                if key not in next_node:
                    next_node[key] = len(terminal)
                    terminal.append(-1)

                node = next_node[key]

            terminal[node] = idx
            pal_words.setdefault(node, []).append(idx)

        answer = []

        # Search each normal word in the reversed trie
        for idx, word in enumerate(words):
            node = 0
            suff = suffix_info[idx]
            matched = True

            for i, ch in enumerate(word):
                other = terminal[node]

                # Trie word ended here.
                # Remaining part of current word must be palindrome.
                if other != -1 and other != idx and suff[i]:
                    answer.append([idx, other])

                key = (node, ch)

                if key not in next_node:
                    matched = False
                    break

                node = next_node[key]

            if not matched:
                continue

            # Current word is fully matched.
            # Remaining part of trie words must be palindrome.
            for other in pal_words.get(node, []):
                if other != idx:
                    answer.append([idx, other])

        return answer