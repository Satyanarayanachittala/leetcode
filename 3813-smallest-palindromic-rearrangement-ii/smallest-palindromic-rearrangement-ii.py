from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 1000001

        freq = Counter(s)

        mid = ""
        half = {}

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ch] = freq[ch] // 2

        total = sum(half.values())

        def comb_cap(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > LIMIT:
                    return LIMIT
            return res

        def count_perm(cnt):
            remain = sum(cnt.values())
            ans = 1
            for ch in sorted(cnt):
                x = cnt[ch]
                if x == 0:
                    continue
                c = comb_cap(remain, x)
                ans *= c
                if ans > LIMIT:
                    return LIMIT
                remain -= x
            return ans

        if count_perm(half) < k:
            return ""

        left = []

        for _ in range(total):
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perm(half)

                if ways >= k:
                    left.append(ch)
                    break
                else:
                    k -= ways
                    half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]