class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        has1 = {}
        has2 = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in has1 and has1[a] != b:
                return False

            if b in has2 and has2[b] != a:
                return False

            has1[a] = b
            has2[b] = a

        return True